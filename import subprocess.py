import subprocess

# filepath: /workspaces/first/test_hello.py


def test_hello_script():
    # Run the hello script
    result = subprocess.run(
        ["python", "/workspaces/first/hello"],
        capture_output=True,
        text=True
    )
    # Check the output
    assert result.stdout == "Hello world!\nHello, world!\n"
    # Ensure the script exits without errors
    assert result.returncode == 0