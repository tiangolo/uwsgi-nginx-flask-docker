import os
import subprocess
import sys

environments = [
    {
        "NAME": "python2.7",
        "BUILD_PATH": "python2.7",
        "TEST_STR1": "Hello World from Flask in a uWSGI Nginx Docker container with Python 2.7 (default)",
        "TEST_STR2": "Hello World from Flask in a uWSGI Nginx Docker container with Python 2.7 - testing",
        "RUN_TESTS": "1",
    },
    {
        "NAME": "python2.7-alpine3.7",
        "BUILD_PATH": "python2.7-alpine3.7",
        "TEST_STR1": "Hello World from Flask in a uWSGI Nginx Docker container with Python 2.7 on Alpine (default)",
        "TEST_STR2": "Hello World from Flask in a uWSGI Nginx Docker container with Python 2.7 - testing",
        "RUN_TESTS": "1",
    },
    {
        "NAME": "python2.7-alpine3.8",
        "BUILD_PATH": "python2.7-alpine3.8",
        "TEST_STR1": "Hello World from Flask in a uWSGI Nginx Docker container with Python 2.7 on Alpine (default)",
        "TEST_STR2": "Hello World from Flask in a uWSGI Nginx Docker container with Python 2.7 - testing",
        "RUN_TESTS": "1",
    },
    {
        "NAME": "python3.5",
        "BUILD_PATH": "python3.5",
        "TEST_STR1": "Hello World from Flask in a uWSGI Nginx Docker container with Python 3.5 (default)",
        "TEST_STR2": "Hello World from Flask in a uWSGI Nginx Docker container with Python 3.5 - testing",
        "RUN_TESTS": "1",
    },
    {
        "NAME": "python3.6",
        "BUILD_PATH": "python3.6",
        "TEST_STR1": "Hello World from Flask in a uWSGI Nginx Docker container with Python 3.6 (default)",
        "TEST_STR2": "Hello World from Flask in a uWSGI Nginx Docker container with Python 3.6 - testing",
        "RUN_TESTS": "1",
    },
    {
        "NAME": "python3.6-alpine3.7",
        "BUILD_PATH": "python3.6-alpine3.7",
        "TEST_STR1": "Hello World from Flask in a uWSGI Nginx Docker container with Python 3.6 on Alpine (default)",
        "TEST_STR2": "Hello World from Flask in a uWSGI Nginx Docker container with Python 3.6 - testing",
        "RUN_TESTS": "1",
    },
    {
        "NAME": "python3.6-alpine3.8",
        "BUILD_PATH": "python3.6-alpine3.8",
        "TEST_STR1": "Hello World from Flask in a uWSGI Nginx Docker container with Python 3.6 on Alpine (default)",
        "TEST_STR2": "Hello World from Flask in a uWSGI Nginx Docker container with Python 3.6 - testing",
        "RUN_TESTS": "1",
    },
    {
        "NAME": "python3.7",
        "BUILD_PATH": "python3.7",
        "TEST_STR1": "Hello World from Flask in a uWSGI Nginx Docker container with Python 3.7 (default)",
        "TEST_STR2": "Hello World from Flask in a uWSGI Nginx Docker container with Python 3.7 - testing",
        "RUN_TESTS": "1",
    },
    {
        "NAME": "latest",
        "BUILD_PATH": "python3.7",
        "TEST_STR1": "Hello World from Flask in a uWSGI Nginx Docker container with Python 3.7 (default)",
        "TEST_STR2": "Hello World from Flask in a uWSGI Nginx Docker container with Python 3.7 - testing",
        "RUN_TESTS": "1",
    },
    {
        "NAME": "python3.7-alpine3.7",
        "BUILD_PATH": "python3.7-alpine3.7",
        "TEST_STR1": "Hello World from Flask in a uWSGI Nginx Docker container with Python 3.7 on Alpine (default)",
        "TEST_STR2": "Hello World from Flask in a uWSGI Nginx Docker container with Python 3.7 - testing",
        "RUN_TESTS": "",
    },
    {
        "NAME": "python3.7-alpine3.8",
        "BUILD_PATH": "python3.7-alpine3.8",
        "TEST_STR1": "Hello World from Flask in a uWSGI Nginx Docker container with Python 3.7 on Alpine (default)",
        "TEST_STR2": "Hello World from Flask in a uWSGI Nginx Docker container with Python 3.7 - testing",
        "RUN_TESTS": "",
    },
    # Index versions
    {
        "NAME": "python2.7-index",
        "BUILD_PATH": "python2.7-index",
        "TEST_STR1": "Hello World from Flask in a uWSGI Nginx Docker container with Python 2.7 (default)",
        "RUN_TESTS": "1",
    },
    {
        "NAME": "python3.5-index",
        "BUILD_PATH": "python3.5-index",
        "TEST_STR1": "Hello World from Flask in a uWSGI Nginx Docker container with Python 3.5 (default)",
        "RUN_TESTS": "1",
    },
    {
        "NAME": "python3.6-index",
        "BUILD_PATH": "python3.6-index",
        "TEST_STR1": "Hello World from Flask in a uWSGI Nginx Docker container with Python 3.6 (default)",
        "RUN_TESTS": "1",
    },
]

start_with = os.environ.get("START_WITH")
build_push = os.environ.get("BUILD_PUSH")


def process_tag(*, env: dict):
    use_env = {**os.environ, **env}
    script = "scripts/test.sh"
    if build_push:
        script = "scripts/build-push.sh"
    return_code = subprocess.call(["bash", script], env=use_env)
    if return_code != 0:
        sys.exit(return_code)


def print_version_envs():
    env_lines = []
    for env in environments:
        env_vars = []
        for key, value in env.items():
            env_vars.append(f"{key}='{value}'")
        env_lines.append(" ".join(env_vars))
    for line in env_lines:
        print(line)


def main():
    start_at = 0
    if start_with:
        start_at = [
            i for i, env in enumerate((environments)) if env["NAME"] == start_with
        ][0]
    for i, env in enumerate(environments[start_at:]):
        print(f"Processing tag: {env['NAME']}")
        process_tag(env=env)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        print_version_envs()
    else:
        main()
