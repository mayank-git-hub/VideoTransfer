import click


@click.group()
def main():
	pass


@main.command()
def server():

	from server import server
	server()


@main.command()
def client():

	from client import client
	client()


if __name__ == "__main__":

	main()
