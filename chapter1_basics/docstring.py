class Person:
    ''' in this file we will learn how to create a docstring
        docstring means that we need to get the html format of this triple quoted lines

        command for executing:
        python -m pydoc -w filename

        we will only enter filename and not the extension.
        example
        python -m pydoc -w abc --> correct
        python -m pydoc -w abc.py --> incorrect

        '''
    def __init__(self, name, age):
        self.name = name
        self.age = age
