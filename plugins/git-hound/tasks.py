import os

from washer.worker.actions import AppendStdout, AppendStderr
from washer.worker.actions import CreateNamedLog, AppendToLog
from washer.worker.actions import AppendHeader
from washer.worker.commands import washertask


@washertask
def main(repopath, prohibited=None, allowed=None, **kwargs):
    import invoke
    c = invoke.Context()

    if prohibited is None:
        prohibited = dict()

    if allowed is None:
        allowed = dict()

    with open(os.path.join(repopath, ".githound.yml"), "w") as config:
        for section, values in [("fail", prohibited),
                                ("skip", allowed)]:

            config.write(f"{section}:\n")
            for name, value in values.items():
                if value.get("type", "regex") == "regex":
                    pattern = value.get("value", None)
                    if pattern:
                        config.write(f"  - {pattern!r}\n")

    with c.cd(repopath):
        res = c.run("git log -p | /git-hound sniff", warn=True)

    yield AppendStdout(res.stdout)
    yield AppendStderr(res.stderr)

    secrets = "\n".join([l for l in res.stdout.splitlines()
                         if l.startswith("failure: ")])
    if secrets:
        # We found something
        yield CreateNamedLog("secrets")
        yield AppendToLog("secrets", secrets)
        # Repo has suspicious data FAILURE!
        return False
    else:
        # Repo is clear SUCCESS!
        return True
