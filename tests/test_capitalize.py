from package.capitalize import capitalize


if capitalize('hello') != 'Hello':
    raise Exception('Wrong working function')

if capitalize('') != '':
    raise Exception('Wrong working function')

print('All tests passed')
