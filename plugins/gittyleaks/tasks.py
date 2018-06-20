from washer.worker.actions import AppendStdout, AppendStderr
from washer.worker.actions import CreateNamedLog, AppendToLog
from washer.worker.commands import washertask


@washertask
def main(repopath, **kwargs):
    import invoke
    c = invoke.Context()

    with c.cd(repopath):
        res = c.run("gittyleaks --find-anything", warn=True)

    yield AppendStdout(res.stdout)
    yield AppendStderr(res.stderr)

    lines = res.stdout.splitlines()
    if lines:
        matches = not (lines[-1] == "No matches.")
        if matches:
            yield CreateNamedLog("secrets")
            yield AppendToLog("secrets", "\n".join(lines[3:]))
            return False

    return True
