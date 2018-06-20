from washer.worker.actions import AppendStdout, AppendStderr
from washer.worker.actions import CreateNamedLog, AppendToLog, AppendHeader
from washer.worker.commands import washertask


@washertask
def main(repopath, prohibited=None, allowed=None, **kwargs):
    import invoke
    c = invoke.Context()

    def add_patterns(patterns, isallowed):
        isallowed = "--allowed" if isallowed else ""
        for name, extra in patterns.items():
            isliteral = "-l" if extra.get("type", "regex") == "literal" else ""
            pattern = extra.get("value", None) 
            if pattern is None:
                yield AppendStderr(f"Invalid pattern {name!r}\n")
            else:
                cmd = f"git secrets --add --global {isallowed} {isliteral} {pattern!r}"
                yield AppendHeader(cmd + "\n")

                res = c.run(cmd, warn=True)
                if res.exited != 0:
                    yield AppendStderr(f"Error adding pattern {name!r}\n")
                else:
                    yield AppendStdout(f"Added pattern {name!r}\n")

    if prohibited is not None:
        yield from add_patterns(prohibited, False)

    if allowed is not None:
        yield from add_patterns(allowed, True)

    with c.cd(repopath):
        res = c.run(f"git secrets --scan-history {repopath!r}",
                    warn=True)

    yield AppendStdout(res.stdout)
    yield AppendStderr(res.stderr)

    found = res.stderr
    if found:
        # We found something
        yield CreateNamedLog("secrets")
        yield AppendToLog("secrets", res.stderr)
        # Repo has suspicious data FAILURE!
        return False
    else:
        # Repo is clear SUCCESS!
        return True
