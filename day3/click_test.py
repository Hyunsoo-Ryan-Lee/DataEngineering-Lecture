import click

@click.command()
@click.option('-s', '--string-to-echo', default="banana")
def click_test(string_to_echo):
    print(string_to_echo)
    
    
if __name__ == '__main__':
    click_test()