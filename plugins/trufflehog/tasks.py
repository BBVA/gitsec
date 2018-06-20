from washer.worker.actions import AppendStdout, AppendStderr
from washer.worker.actions import CreateNamedLog, AppendToLog
from washer.worker.commands import washertask


@washertask
def main(repopath, **kwargs):
    import invoke
    c = invoke.Context()

    res = c.run("trufflehog --json %r" % repopath, warn=True)

    yield AppendStdout(res.stdout)
    yield AppendStderr(res.stderr)

    if res.stdout:
        # We found something
        yield CreateNamedLog("secrets")
        yield AppendToLog("secrets", res.stdout)
        # Repo has suspicious data FAILURE!
        return False
    else:
        # Repo is clear SUCCESS!
        return True
