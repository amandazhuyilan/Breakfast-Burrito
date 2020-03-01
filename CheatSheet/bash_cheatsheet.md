- To install packages non-interactively, do:
```shell
export DEBIAN_FRONTEND=noninteractive
apt-get update && apt install --fix-missing -y -q \
	my_lovely_app
```
