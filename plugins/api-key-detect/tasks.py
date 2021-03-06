from washer.worker.actions import AppendStdout, AppendStderr
from washer.worker.actions import CreateNamedLog, AppendToLog
from washer.worker.commands import washertask


@washertask
def main(repopath, **kwargs):
    import invoke
    c = invoke.Context()

    res = c.run("python /api-key-detect/api_key_detect.py %r" % repopath,
                warn=True)

    yield AppendStdout(res.stdout)
    yield AppendStderr(res.stderr)

    found = "Line" in res.stdout and "Entropy" in res.stdout
    if found:
        # We found something
        yield CreateNamedLog("secrets")
        yield AppendToLog(
            "secrets",
            "\n".join(res.stdout.splitlines()[3:]))
        # Repo has suspicious data FAILURE!
        return False
    else:
        # Repo is clear SUCCESS!
        return True
