name: workflow
on: [push]
jobs:
  helloworld:
    runs-on: ubuntu-latest
    steps:
    - name: workflow
      run: echo "Hello, World!"
