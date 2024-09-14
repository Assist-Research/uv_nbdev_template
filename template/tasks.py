from invoke import task


@task
def prepare(c):
    c.run("nbdev_prepare")
    c.run("nbdev_docs")


@task
def check(c):
    c.run("pre-commit run --all-files")
