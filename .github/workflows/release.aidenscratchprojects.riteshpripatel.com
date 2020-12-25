name: Release.aidenscratchprojects.riteshpripatel.com
on:
  push:
    branches:
      - master
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v1
    - name: Release to S3
      run: bash scripts/pipeline/release.sh aidenscratchprojects.riteshpripatel.com aidencode/html/aidenscratchprojects/index.html ${{secrets.AWS_ACCESS_KEY}} ${{secrets.AWS_ACCESS_SECRET}} "/"
