from termcolor import colored, cprint


def text_msg(str, underline=False):
	attrs = ['bold']
	if underline:
		attrs.append('underline')
	return colored(str, 'white', attrs = attrs)

def text_success(str, underline=False):
	attrs = ['bold']
	if underline:
		attrs.append('underline')
	return colored(str, 'green', attrs = attrs)
