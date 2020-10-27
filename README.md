# protobuf_options_example
Example on reading custom options from protobuf file descriptor sets.

# Description

Compiles a file descriptor set from a proto that defines a service with a custom option on some methods (in this case, the option is a boolean "unsecured" flag).

Also, compiles in python the proto containing the descriptor - compilation **only of this proto file** is necessary.

Finally, a python script loads the file descriptor set and prints, for each method, the value of the custom option.

# Caveats

The file descriptor set contains all the information. However, it's necessary to have the compiled proto **of the annotation** in python to be able to access it's value.

Therefore, a simple compilation of only this file is enough.

# Running the example

To run, first install dependencies and init pipenv:

```bash
$ pipenv install
```

Build the descriptor set and compile the proto descriptor.

```bash
$ pipenv run build.sh
```

Run the script

```
$ pipenv run python main.py
```
