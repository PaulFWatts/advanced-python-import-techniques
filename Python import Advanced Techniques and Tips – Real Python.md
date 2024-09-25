Watch Now This tutorial has a related video course created by the Real Python team. Watch it together with the written tutorial to deepen your understanding: [**Advanced Python import Techniques**](https://realpython.com/courses/advanced-import-techniques/)

In Python, you use the **`import`** keyword to make code in one **module** available in another. Imports in Python are important for **structuring your code** effectively. Using imports properly will make you more productive, allowing you to reuse code while keeping your projects maintainable.

This tutorial will provide a thorough overview of Python’s `import` statement and how it works. The import system is powerful, and you’ll learn how to harness this power. While you’ll cover many of the concepts behind Python’s import system, this tutorial is mostly example driven. You’ll learn from several code examples throughout.

**In this tutorial, you’ll learn how to:**

-   Use **modules**, **packages**, and **namespace packages**
-   Handle **resources** and **data files** inside your packages
-   Import modules **dynamically** at runtime
-   **Customize** Python’s import system

Throughout the tutorial, you’ll see examples of how to play with the Python import machinery in order to work most efficiently. While all the code is shown in the tutorial, you can also download it by clicking the box below:

## Basic Python `import`

Python code is organized into both [modules and packages](https://realpython.com/python-modules-packages). This section will explain how they differ and how you can work with them.

Later in the tutorial, you’ll see some advanced and lesser-known uses of Python’s import system. However, let’s get started with the basics: importing modules and packages.

### Modules

The [Python.org glossary](https://docs.python.org/glossary.html) defines **module** as follows:

> An object that serves as an organizational unit of Python code. Modules have a namespace containing arbitrary Python objects. Modules are loaded into Python by the process of importing. ([Source](https://docs.python.org/glossary.html#term-module))

In practice, a module usually corresponds to one `.py` file containing Python code.

The true power of modules is that they can be imported and reused in other code. Consider the following example:

In the first line, `import math`, you import the code in the [`math` module](https://realpython.com/python-math-module/) and make it available to use. In the second line, you access the `pi` [variable](https://realpython.com/python-variables/) within the `math` module. `math` is part of [Python’s standard library](https://docs.python.org/library/index.html), which means that it’s always available to import when you’re running Python.

Note that you write `math.pi` and not just simply `pi`. In addition to being a module, `math` acts as a [**namespace**](https://realpython.com/python-namespaces-scope/) that keeps all the attributes of the module together. Namespaces are useful for keeping your code readable and organized. In the words of Tim Peters:

> Namespaces are one honking great idea—let’s do more of those! ([Source](https://www.python.org/dev/peps/pep-0020/))

You can list the contents of a namespace with `dir()`:

Using `dir()` without any argument shows what’s in the global namespace. To see the contents of the `math` namespace, you use `dir(math)`.

You’ve already seen the most straightforward use of `import`. However, there are other ways to use it that allow you to import specific parts of a module and to rename the module as you import it.

The following code imports only the `pi` variable from the `math` module:

Note that this places `pi` in the global namespace and not within a `math` namespace.

You can also rename modules and attributes as they’re imported:

For more details about the syntax for importing modules, check out [Python Modules and Packages – An Introduction](https://realpython.com/python-modules-packages/#the-import-statement).

### Packages

You can use a package to further organize your modules. The Python.org glossary defines **package** as follows:

> A Python module which can contain submodules or recursively, subpackages. Technically, a package is a Python module with an `__path__` attribute. ([Source](https://docs.python.org/glossary.html#term-package))

Note that a package is still a module. As a user, you usually don’t need to worry about whether you’re importing a module or a package.

In practice, a package typically corresponds to a file directory containing Python files and other directories. To create a Python package yourself, you create a directory and a [file named `__init__.py`](https://docs.python.org/reference/import.html#regular-packages) inside it. The `__init__.py` file contains the contents of the package when it’s treated as a module. It can be left empty.

In general, submodules and subpackages aren’t imported when you import a package. However, you can use `__init__.py` to include any or all submodules and subpackages if you want. To show a few examples of this behavior, you’ll create a package for saying [`Hello world`](http://helloworldcollection.de/) in a few different languages. The package will consist of the following directories and files:

```
<span></span><code>world/
│
├── africa/
│   ├── __init__.py
│   └── zimbabwe.py
│
├── europe/
│   ├── __init__.py
│   ├── greece.py
│   ├── norway.py
│   └── spain.py
│
└── __init__.py
</code>
```

Each country file [prints](https://realpython.com/python-print/) out a greeting, while the `__init__.py` files selectively import some of the subpackages and submodules. The exact contents of the files are as follows:

Note that `world/__init__.py` imports only `africa` and not `europe`. Similarly, `world/africa/__init__.py` doesn’t import anything, while `world/europe/__init__.py` imports `greece` and `norway` but not `spain`. Each country module will print a greeting when it’s imported.

Let’s play with the `world` package at the interactive prompt to get a better understanding of how the subpackages and submodules behave:

When `europe` is imported, the `europe.greece` and `europe.norway` modules are imported as well. You can see this because the country modules print a greeting when they’re imported:

The `world/africa/__init__.py` file is empty. This means that importing the `world.africa` package creates the namespace but has no other effect:

Remember, importing a module both loads the contents and creates a namespace containing the contents. The last few examples show that it’s possible for the same module to be part of different namespaces.

It’s fairly common to import subpackages and submodules in an `__init__.py` file to make them more readily available to your users. You can see [one example of this](https://github.com/psf/requests/blob/v2.23.0/requests/__init__.py#L112) in the popular [`requests` package](https://realpython.com/python-requests/).

### Absolute and Relative Imports

Recall the source code of `world/__init__.py` in the earlier example:

You’ve already seen `from...import` statements such as `from math import pi`, but what does the dot (`.`) in `from . import africa` mean?

The dot refers to the current package, and the statement is an example of a **relative import**. You can read it as “From the current package, import the subpackage `africa`.”

There’s an equivalent **absolute import** statement in which you explicitly name the current package:

In fact, all imports in `world` could have been done explicitly with similar absolute imports.

Relative imports must be in the form `from...import`, and the location you’re importing from must start with a dot.

The [PEP 8 style guide](https://www.python.org/dev/peps/pep-0008/#imports) recommends using absolute imports in general. However, relative imports are an alternative for organizing package hierarchies. For more information, see [Absolute vs Relative Imports in Python](https://realpython.com/absolute-vs-relative-python-imports/).

### Python’s Import Path

How does Python find the modules and packages it imports? You’ll see more details about the mechanics of the Python import system [later](https://realpython.com/python-import/#import-internals). For now, just know that Python looks for modules and packages in its [**import path**](https://docs.python.org/glossary.html#term-import-path). This is a list of locations that are searched for modules to import.

You can inspect Python’s import path by printing `sys.path`. Broadly speaking, this list will contain three different kinds of locations:

1.  The directory of the current script (or the current directory if there’s no script, such as when Python is running interactively)
2.  The contents of the `PYTHONPATH` environment variable
3.  Other, installation-dependent directories

Typically, Python will start at the beginning of the list of locations and look for a given module in each location until the first match. Since the script directory or the current directory is always first in this list, you can make sure that your scripts find your self-made modules and packages by organizing your directories and being careful about which directory you run Python from.

However, you should also be careful that you don’t create modules that **shadow**, or hide, other important modules. As an example, say that you define the following `math` module:

Using this module works as expected:

But this module also shadows the `math` module that’s included in the standard library. Unfortunately, that means our earlier example of looking up the value of π no longer works:

The problem is that Python now searches your new `math` module for `pi` instead of searching the `math` module in the standard library.

To avoid these kinds of issues, you should be careful with the names of your modules and packages. In particular, your top-level module and package names should be unique. If `math` is defined as a submodule within a package, then it won’t shadow the built-in module.

### Example: Structure Your Imports

While it’s possible to organize your imports by using the current directory as well as by manipulating `PYTHONPATH` and even `sys.path`, the process is often unruly and prone to errors. To see a typical example, consider the following application:

```
<span></span><code>structure/
│
├── files.py
└── structure.py
</code>
```

The app will re-create a given file structure by creating directories and empty files. The `structure.py` file contains the main script, and `files.py` is a library module with a few functions for dealing with files. The following is an example of output from the app, in this case by running it in the `structure` directory:

The two source code files as well as the automatically created `.pyc` file are re-created inside a new directory named `001`.

Now take a look at the source code. The main functionality of the app is defined in `structure.py`:

In **lines 12 to 16**, you read a root path from the command line. In the above example you use a dot, which means the current directory. This path will be used as the `root` of the file hierarchy that you’ll re-create.

The actual work happens in **lines 19 to 23**. First, you create a unique path, `new_root`, that will be the root of your new file hierarchy. Then you loop through all paths below the original `root` and re-create them as empty files inside the new file hierarchy.

For manipulating paths like this, `pathlib` in the standard library is quite useful. For more details on how it’s used, check out [Python’s `pathlib` Module: Taming the File System](https://realpython.com/python-pathlib/).

On **line 26**, you call `main()`. You’ll learn more about the `if` test on **line 25** [later](https://realpython.com/python-import/#import-scripts-as-modules). For now, you should know that the special variable `__name__` has the value `__main__` inside scripts, but it gets the name of the module inside imported modules. For more information on `__name__`, check out [Defining Main Functions in Python](https://realpython.com/python-main-function/#use-__name__-to-control-the-execution-of-your-code) and [What Does if **name** == “**main**” Do in Python?](https://realpython.com/if-name-main-python/).

Note that you import `files` on **line 8**. This library module contains two utility functions:

`unique_path()` [uses a counter](https://realpython.com/python-pathlib/#create-a-unique-file-name) to find a path that doesn’t already exist. In the app, you use it to find a unique subdirectory to use as the `new_root` of the re-created file hierarchy. Next, `add_empty_file()` makes sure all necessary directories are created before creating an empty file using [`.touch()`](https://docs.python.org/library/pathlib.html#pathlib.Path.touch).

Have a look at the import of `files` again:

It looks quite innocent. However, as the project grows, this line will cause you some headaches. Even though you import `files` from the `structure` project, the import is **absolute**: it doesn’t start with a dot. This means that `files` must be found in the import path for the import to work.

Luckily, the directory containing the current script is always in Python’s import path, so this works fine for now. However, if your project gains some traction, then it may be used in other ways.

For example, someone might want to import the script into a [Jupyter Notebook](https://realpython.com/jupyter-notebook-introduction/) and run it from there. Or they may want to reuse the `files` library in another project. They may even [create an executable with PyInstaller](https://realpython.com/pyinstaller-python/) to more easily distribute it. Unfortunately, any of these scenarios can create issues with the import of `files`.

To see an example, you can follow the PyInstaller guide and [create an entry point to your application](https://realpython.com/pyinstaller-python/#preparing-your-project). Add an extra directory outside your application directory:

```
<span></span><code>structure/
│
├── structure/
│   ├── files.py
│   └── structure.py
│
└── cli.py
</code>
```

In the outer directory, create the entry point script, `cli.py`:

This script will import `main()` from your original script and run it. Note that `main()` isn’t run when `structure` is imported because of the `if` test on **line 25** in `structure.py`. That means you need to run `main()` explicitly.

In theory, this should work similarly to running the app directly:

Why didn’t that work? Suddenly, the import of `files` raises an error.

The problem is that by starting the app with `cli.py`, you’ve changed the location of the current script, which in turn changes the import path. `files` is no longer on the import path, so it can’t be imported absolutely.

One possible solution is to change Python’s import path:

This works because the import path includes the folder containing `structure.py` and `files.py`. The issue with this approach is that your import path can get very messy and hard to understand.

In practice, you’re re-creating a feature of early Python versions called **implicit relative imports**. These were removed from the language by [PEP 328](https://www.python.org/dev/peps/pep-0328/) with the following rationale:

> In Python 2.4 and earlier, if you’re reading a module located inside a package, it is not clear whether `import foo` refers to a top-level module or to another module inside the package. As Python’s library expands, more and more existing package internal modules suddenly shadow standard library modules by accident. It’s a particularly difficult problem inside packages because there’s no way to specify which module is meant. ([Source](https://www.python.org/dev/peps/pep-0328/#rationale-for-absolute-imports))

Another solution is to use a relative import instead. Change the import in `structure.py` as follows:

You can now start your app through the entry point script:

Unfortunately, you can no longer call the app directly:

The problem is that [relative imports are resolved differently in scripts](https://www.python.org/dev/peps/pep-0328/#relative-imports-and-name) than are imported modules. Of course, you could go back and restore the absolute import before running the script directly, or you could even do some `try...except` acrobatics to import files absolutely or relatively depending on what works.

There’s even an [officially sanctioned hack](https://www.python.org/dev/peps/pep-0366/) to make relative imports work in scripts. Unfortunately, this also forces you to change `sys.path` in most cases. To quote [Raymond Hettinger](https://twitter.com/raymondh):

> There must be a better way! ([Source](https://youtu.be/wf-BqAjZb8M?t=23m07s))

Indeed, a better—and more stable—solution is to play along with Python’s import and packaging system and install your project as a local package [using `pip`](https://realpython.com/what-is-pip/).

### Create and Install a Local Package

When you install a package from [PyPI](https://pypi.org/), that package is available to all scripts in your environment. However, you can also install packages from your local computer, and they’ll also be made available in the same way.

Creating a local package doesn’t involve much overhead. First, create minimal [`setup.cfg`](https://setuptools.readthedocs.io/en/latest/setuptools.html#configuring-setup-using-setup-cfg-files) and [`setup.py`](https://snarky.ca/what-the-heck-is-pyproject-toml/#how-to-use-pyproject-toml-with-setuptools) files in the outer `structure` directory:

In theory, the `name` and `version` can be whatever you like. However, they’ll be used by `pip` when referring to your package, so you should choose values that are recognizable and don’t collide with other packages you use.

One tip is to give all such local packages a common prefix like `local_` or your username. `packages` should list the directory or directories containing your source code. You can then install the package locally using `pip`:

This command will install the package to your system. `structure` will then be found on Python’s import path, meaning you can use it anywhere without having to worry about the script directory, relative imports, or other complications. The `-e` option stands for **editable**, which is important because it allows you to change the source code of your package without reinstalling it.

Now that `structure` is installed on your system, you can use the following import statement:

This will work no matter how you end up calling your application.

While it’s a good idea to separate scripts and libraries, all Python files can be both executed and imported. In a [later section](https://realpython.com/python-import/#import-scripts-as-modules), you’ll learn more about how to create modules that handle both well.

### Namespace Packages

Python modules and packages are very closely related to files and directories. This sets Python apart from many other programming languages in which packages merely act as namespaces without enforcing how the source code is organized. See the discussion in [PEP 402](https://www.python.org/dev/peps/pep-0402/#the-problem) for examples.

**Namespace packages** have been available in Python since version 3.3. These are less dependent on the underlying file hierarchy. In particular, namespace packages can be split across multiple directories. A namespace package is created automatically if you have a directory containing a `.py` file but no `__init__.py`. See [PEP 420](https://www.python.org/dev/peps/pep-0420/) for a detailed explanation.

To get a better understanding of why namespace packages can be useful, let’s try to implement one. As a motivating example, you’ll have another go at the problem solved in [The Factory Method Pattern and Its Implementation in Python](https://realpython.com/factory-method-python/): given a `Song` object, you want to convert it to one of several string representations. In other words, you want to **serialize** `Song` objects.

To be more concrete, you want to implement code that works something like this:

Let’s assume that you’re lucky and come across a [third-party implementation](https://realpython.com/factory-method-python/#an-object-serialization-example) of several of the formats that you need to serialize to, and it’s organized as a namespace package:

```
<span></span><code>third_party/
│
└── serializers/
    ├── json.py
    └── xml.py
</code>
```

The file `json.py` contains code that can serialize an object to the [JSON format](https://realpython.com/python-json/):

This serializer interface is a bit limited, but it’ll be enough to demonstrate how namespace packages work.

The file `xml.py` contains a similar `XmlSerializer` that can convert an object to [XML](https://www.xml.com/axml/axml.html):

Note that both of these classes implement the same interface with `.start_object()`, `.add_property()`, and `.__str__()` methods.

You then create a `Song` class that can use these serializers:

A `Song` is defined by its ID, title, and artist. Note that `.serialize()` doesn’t need to know which format it converts to because it uses the common interface defined earlier.

Assuming that you’ve installed the third-party `serializers` package, you can use it as follows:

By providing different serializer objects to `.serialize()`, you get different representations of your song.

So far, so good. However, now you realize that you also need to convert your songs to a [YAML](https://realpython.com/python-yaml/) representation, which is not supported in the third-party library. Enter the magic of namespace packages: you can add your own `YamlSerializer` to the `serializers` package without touching the third-party library.

First, create a directory on your local file system called `serializers`. It’s important that the name of the directory matches the name of the namespace package that you’re customizing:

```
<span></span><code>local/
│
└── serializers/
    └── yaml.py
</code>
```

In the `yaml.py` file, you define your own `YamlSerializer`. You base this on the [`PyYAML` package](https://pypi.org/project/PyYAML/), which must be installed from PyPI:

Since YAML and JSON are quite similar formats, you can reuse most of the implementation of `JsonSerializer`:

Note that the `YamlSerializer` is based on the `JsonSerializer`, which is imported from `serializers` itself. Since both `json` and `yaml` are part of the same namespace package, you could even use a relative import: `from .json import JsonSerializer`.

Continuing the above example, you can now convert the song to YAML as well:

Just like regular modules and packages, namespace packages must be found on the Python import path. If you were following along with the previous examples, then you might have had issues with Python not finding `serializers`. In actual code, you would have used `pip` to install the third-party library, so it would be in your path automatically.

You should also make sure that your local library is available like a normal package. As explained above, you can do this either by running Python from the proper directory or by using `pip` to install the local library as well.

In this example, you’re testing how to integrate a fake third-party package with your local package. If `third_party` were a real package, then you would download it from PyPI using `pip`. Since this isn’t possible, you can simulate it by installing `third_party` locally like you did in the [`structure` example earlier](https://realpython.com/python-import/#example-structure-your-imports).

Alternatively, you can mess with your import path. Put the `third_party` and `local` directories inside the same folder, then customize your Python path as follows:

You can now use all serializers without worrying about whether they’re defined in the third-party package or locally.

### Imports Style Guide

[PEP 8](https://www.python.org/dev/peps/pep-0008/), the Python style guide, has a couple of [recommendations about imports](https://www.python.org/dev/peps/pep-0008/#imports). As always with Python, keeping your code both readable and maintainable is an important consideration. Here are a few general rules of thumb for how to style your imports:

-   Keep imports at the top of the file.
-   Write imports on separate lines.
-   Organize imports into groups: first standard library imports, then third-party imports, and finally local application or library imports.
-   Order imports alphabetically within each group.
-   Prefer absolute imports over relative imports.
-   Avoid wildcard imports like `from module import *`.

[`isort`](https://pypi.org/project/isort/) and [`reorder-python-imports`](https://pypi.org/project/reorder-python-imports/) are great tools for enforcing a consistent style on your imports.

Here’s an example of an import section inside the [_Real Python_ feed reader package](https://github.com/realpython/reader/blob/master/reader/feed.py):

Note how this grouping makes the [dependencies](https://realpython.com/courses/managing-python-dependencies/) of this module clear: `feedparser` and `html2text` need to be installed on the system. You can generally assume that the standard library is available. Separating imports from within your package gives you some overview over the internal dependencies of your code.

There are cases in which it makes sense to bend these rules a little. You’ve already seen that relative imports can be an alternative to organizing package hierarchies. [Later](https://realpython.com/python-import/#handle-cyclical-imports), you’ll see how in some cases you can move imports into a function definition to break import cycles.

## Resource Imports

Sometimes you’ll have code that depends on data files or other resources. In small scripts, this isn’t a problem—you can specify the path to your data file and carry on!

However, if the resource file is important for your package and you want to distribute your package to other users, then a few challenges will arise:

1.  You won’t have control over the path to the resource since that will depend on your user’s setup as well as on how the package is distributed and installed. You can try to figure out the resource path based on your package’s `__file__` or `__path__` attributes, but this may not always work as expected.
    
2.  Your package may [reside inside a ZIP file](https://realpython.com/python-import/#run-python-scripts-from-zip-files) or an old [`.egg` file](https://packaging.python.org/discussions/wheel-vs-egg/), in which case the resource won’t even be a physical file on the user’s system.
    

There have been several attempts at solving these challenges, including [`setuptools.pkg_resources`](https://setuptools.readthedocs.io/en/latest/pkg_resources.html). However, with the introduction of `importlib.resources` into the standard library in [Python 3.7](https://realpython.com/python37-new-features/#importing-data-files-with-importlibresources), there’s now one standard way of dealing with resource files.

### Introducing `importlib.resources`

[`importlib.resources`](https://docs.python.org/library/importlib.html) gives access to resources within packages. In this context, a **resource** is any file located within an importable package. The file may or may not correspond to a physical file on the file system.

This has a couple of advantages. By reusing the import system, you get a more consistent way of dealing with the files inside your packages. It also gives you easier access to resource files in other packages. The documentation sums it up nicely:

> If you can import a package, you can access resources within that package. ([Source](https://docs.python.org/library/importlib.html#module-importlib.resources))

`importlib.resources` became part of the standard library in Python 3.7. However, on older versions of Python, a [backport is available as `importlib_resources`](https://importlib-resources.readthedocs.io/). To use the backport, install it from [PyPI](https://pypi.org/project/importlib_resources/):

The backport is compatible with Python 2.7 as well as Python 3.4 and later versions.

There’s one requirement when using `importlib.resources`: your resource files must be available inside a regular package. Namespace packages aren’t supported. In practice, this means that the file must be in a directory containing an `__init__.py` file.

As a first example, assume you have [resources](https://www.gutenberg.org/ebooks/11) inside a package like this:

```
<span></span><code>books/
│
├── __init__.py
├── alice_in_wonderland.png
└── alice_in_wonderland.txt
</code>
```

`__init__.py` is just an empty file necessary to designate `books` as a regular package.

You can then use `open_text()` and `open_binary()` to open text and binary files, respectively:

`open_text()` and `open_binary()` are equivalent to the built-in `open()` with the `mode` parameter set to `rt` and `rb`, respectively. Convenient functions for reading text or binary files directly are also available as `read_text()` and `read_binary()`. See the [official documentation](https://docs.python.org/library/importlib.html#module-importlib.resources) for more information.

The rest of this section will show a few elaborate examples of using resource files in practice.

### Example: Use Data Files

As a more complete example of using data files, you’ll see how to implement a quiz program based on [United Nations population data](https://population.un.org/wpp/). First, create a `data` package and download [`WPP2019_TotalPopulationBySex.csv`](https://population.un.org/wpp/Download/Files/1_Indicators%20(Standard)/CSV_FILES/WPP2019_TotalPopulationBySex.csv) from [the UN web page](https://population.un.org/wpp/Download/Standard/CSV/):

```
<span></span><code>data/
│
├── __init__.py
└── WPP2019_TotalPopulationBySex.csv
</code>
```

Open the CSV file and have a look at the data:

Each line contains the population of a country for a given year and a given variant, which indicates what kind of scenario is used for the projection. The file contains population projections until the year 2100.

The following function reads this file and picks out the total population of each country for a given `year` and `variant`:

The highlighted lines show how `importlib.resources` is used to open the data file. For more information about working with CSV files, check out [Reading and Writing CSV Files in Python](https://realpython.com/python-csv/).

The above function returns a dictionary with population numbers:

You can do any number of interesting things with this population dictionary, including analysis and visualizations. Here, you’ll create a quiz game that asks users to identify which country in a set is most populous. Playing the game will look something like this:

The details of the implementation are too far outside the topic of this tutorial, so they won’t be discussed here. However, you can expand the section below to see the complete source code.

### Example: Add Icons to Tkinter GUIs

When building graphical user interfaces (GUIs), you often need to include resource files like icons. The following example shows how you can do that using `importlib.resources`. The final app will look quite basic, but it’ll have a custom icon as well as an illustration on the _Goodbye_ button:

[![A small GUI with custom icons](https://files.realpython.com/media/imports-hello-gui.305aa8c61d9e.png)](https://files.realpython.com/media/imports-hello-gui.305aa8c61d9e.png)

The example uses [Tkinter](https://realpython.com/python-gui-tkinter), which is a GUI package available in the standard library. It’s based on the [Tk](https://tcl.tk/) windowing system, originally developed for the Tcl programming language. There are many other GUI packages available for Python. If you’re using a different one, then you should be able [add icons to your app](https://realpython.com/python-pyqt-layout/) using ideas similar to the ones presented here.

In Tkinter, images are handled by the [`PhotoImage` class](http://effbot.org/tkinterbook/photoimage.htm). To create a `PhotoImage`, you pass in a path to an image file.

Remember, when distributing your package, you’re not even guaranteed that resource files will exist as physical files on the file system. `importlib.resources` solves this by providing `path()`. This function will return a [path](https://realpython.com/python-pathlib/) to the resource file, creating a temporary file if necessary.

To make sure any temporary files are cleaned up properly, you should use `path()` as a context manager using the keyword `with`:

For the full example, assume you have the following file hierarchy:

```
<span></span><code>hello_gui/
│
├── gui_resources/
│   ├── __init__.py
│   ├── hand.png
│   └── logo.png
│
└── __main__.py
</code>
```

If you want to try the example yourself, then you can download these files along with the rest of the source code used in this tutorial by clicking the link below:

The code is stored in a file with the special name `__main__.py`. This name indicates that the file is the entry point for the package. Having a `__main__.py` file allows your package to be executed with `python -m`:

For more information on calling a package with `-m`, see [How to Publish an Open-Source Python Package to PyPI](https://realpython.com/pypi-publish-python-package/#different-ways-of-calling-a-package).

The GUI is defined in a class called `Hello`. Note that you use `importlib.resources` to obtain the path of the image files:

If you want to learn more about building GUIs with Tkinter, then check out [Python GUI Programming With Tkinter](https://realpython.com/python-gui-tkinter/). The official documentation also has a [nice list of resources](https://docs.python.org/library/tkinter.html) to start with, and the [tutorial at TkDocs](https://tkdocs.com/tutorial/) is another great resource that shows how to use Tk in other languages.

To make sure that the images are kept around, you should manually add a reference to them. You can see examples of this in the code above on **lines 18 and 31**.

## Dynamic Imports

One of Python’s defining features is that it’s a very dynamic language. Although it’s sometimes a bad idea, you can do many things to a Python program when it’s running, including adding attributes to a class, redefining methods, or changing the [docstring](https://realpython.com/documenting-python-code/#documenting-your-python-code-base-using-docstrings) of a module. For instance, you can change `print()` so that it doesn’t do anything:

Technically, you’re not redefining `print()`. Instead, you’re defining _another_ `print()` that shadows the built-in one. To return to using the original `print()`, you can delete your custom one with `del print`. If you’re so inclined, you can shadow any Python object that is built into the interpreter.

In this section, you’ll learn how to do **dynamic imports** in Python. With them, you won’t have to decide what to import until your program is running.

### Using `importlib`

So far, you’ve used Python’s `import` keyword to import modules and packages explicitly. However, the whole import machinery is available in the `importlib` package, and this allows you to do your imports more dynamically. The following script asks the user for the name of a module, imports that module, and prints its docstring:

`import_module()` returns a module object that you can bind to any variable. Then you can treat that variable as a regularly imported module. You can use the script like this:

In each case, the module is imported dynamically by `import_module()`.

### Example: Factory Method With Namespace Packages

Think back to the [serializers example](https://realpython.com/python-import/#namespace-packages) from earlier. With `serializers` implemented as a namespace package, you had the ability to add custom serializers. In the [original example](https://realpython.com/factory-method-python/#an-object-serialization-example) from a previous tutorial, the serializers were made available through a serializer factory. Using `importlib`, you can do something similar.

Add the following code to your local `serializers` namespace package:

The `get_serializer()` factory can create serializers dynamically based on the `format` parameter, and `serialize()` can then apply the serializer to any object that implements a `.serialize()` method.

The factory makes some strong assumptions about the naming of both the module and the class containing the individual serializers. In the [next section](https://realpython.com/python-import/#example-a-package-of-plugins), you’ll learn about a plugin architecture that allows more flexibility.

You can now re-create the earlier example as follows:

In this case, you no longer need to explicitly import each serializer. Instead, you specify the name of a serializer with a string. The string could even be chosen by your user at runtime.

The final example shows that you also get a decent error message if you try to serialize to a format that hasn’t been implemented.

### Example: A Package of Plugins

Let’s look at another example of using dynamic imports. You can use the following module to set up a flexible plugin architecture in your code. This is similar to the previous example, in which you could plug in serializers for different formats by adding new modules.

One application that uses plugins effectively is the [Glue exploratory visualization tool](http://glueviz.org/). Glue can read many different data formats out of the box. However, if your data format isn’t supported, then you can write your own [custom data loader](http://docs.glueviz.org/en/stable/customizing_guide/customization.html#custom-data-loaders).

You do this by adding a function that you decorate and place in a special location to make it easy for Glue to find. You don’t need to alter any part of the Glue source code. See the [documentation](http://docs.glueviz.org/) for all the details.

You can set up a similar plugin architecture that you can use in your own projects. Within the architecture, there are two levels:

1.  **A plugin package** is a collection of related plugins corresponding to a Python package.
2.  **A plugin** is a custom behavior made available in a Python module.

The `plugins` module that exposes the plugin architecture has the following functions:

The factory functions are used to conveniently add functionality to plugin packages. You’ll see some examples of how they’re used shortly.

Looking at all the details of this code is outside the scope of this tutorial. If you’re interested, then you can see an implementation by expanding the section below.

Let’s look at some examples of how to use plugins. The first example is a `greeter` package that you can use to add many different greetings to your app. A full plugin architecture is definitely overkill for this example, but it shows how the plugins work.

Assume you have the following `greeter` package:

```
<span></span><code>greeter/
│
├── __init__.py
├── hello.py
├── howdy.py
└── yo.py
</code>
```

Each `greeter` module defines a function that takes one `name` argument. Note how they’re all registered as plugins using the `@register` decorator:

To learn more about decorators and how they’re used, check out [Primer on Python Decorators](https://realpython.com/primer-on-python-decorators/).

To finish setting up `greeter` as a plugin package, you can use the factory functions in `plugins` to add functionality to the `greeter` package itself:

You can now use `greetings()` and `greet()` as follows:

Note that `greetings()` automatically discovers all the plugins that are available in the package.

You can also more dynamically choose which plugin to call. In the following example, you choose a plugin at random. However, you could also select a plugin based on a configuration file or user input:

To discover and call the different plugins, you need to import them. Let’s have a quick look at how `plugins` handles imports. The main work is done in the following two functions inside `plugins.py`:

`_import()` looks deceptively straightforward. It uses `importlib` to import a module. But there are a couple of things also happening in the background:

1.  Python’s import system ensures that each plugin is imported only once.
2.  `@register` decorators defined inside each plugin module register each imported plugin.
3.  In a full implementation, there would also be some error handling to deal with missing plugins.

`_import_all()` discovers all the plugins within a package. Here’s how it works:

1.  `contents()` from `importlib.resources` lists all the files inside a package.
2.  The results are filtered to find potential plugins.
3.  Each Python file not starting with an underscore is imported.
4.  Plugins in any of the files are discovered and registered.

Let’s end this section with a final version of the [serializers namespace package](https://realpython.com/python-import/#example-factory-method-with-namespace-packages). One outstanding issue was that the `get_serializer()` factory made strong assumptions about the naming of the serializer classes. You can make this more flexible using plugins.

First, add a line registering each of the serializers. Here is an example of how it’s done in the `yaml` serializer:

Next, update `get_serializers()` to use `plugins`:

You implement `get_serializer()` using `call_factory()` since that will automatically instantiate each serializer. With this refactoring, the serializers work just the same as earlier. However, you have more flexibility in naming your serializer classes.

For more information about using plugins, check out [PyPlugs](https://pypi.org/project/pyplugs/) on PyPI and the [Plug-ins: Adding Flexibility to Your Apps](https://github.com/gahjelle/talks/tree/master/20190505_pycon_plugins/) presentation from [PyCon 2019](https://us.pycon.org/2019/).

## The Python Import System

You’ve seen many ways to take advantage of Python’s import system. In this section, you’ll learn a bit more about what happens behind the scenes as modules and packages are imported.

As with most parts of Python, the import system can be customized. You’ll see several ways that you can change the import system, including automatically downloading missing packages from PyPI and importing data files as if they were modules.

### Import Internals

The details of the Python import system are described in [the official documentation](https://docs.python.org/reference/import.html). At a high level, three things happen when you import a module (or package). The module is:

1.  Searched for
2.  Loaded
3.  Bound to a namespace

For the usual imports—those done with the `import` statement—all three steps happen automatically. When you use `importlib`, however, only the first two steps are automatic. You need to bind the module to a variable or namespace yourself.

For instance, the following methods of importing and renaming `math.pi` are roughly equivalent:

Of course, in normal code you should prefer the former.

One thing to note is that, even when you import only one attribute from a module, the whole module is loaded and executed. The rest of the contents of the module just aren’t bound to the current namespace. One way to prove this is to have a look at what’s known as the **module cache**:

`sys.modules` acts as a module cache. It contains references to all modules that have been imported.

The module cache plays a very important role in the Python import system. The first place Python looks for modules when doing an import is in `sys.modules`. If a module is already available, then it isn’t loaded again.

This is a great optimization, but it’s also a necessity. If modules were reloaded each time they were imported, then you could end up with inconsistencies in certain situations, such as when the underlying source code changes while a script is running.

Recall the [import path](https://realpython.com/python-import/#pythons-import-path) you saw earlier. It essentially tells Python where to search for modules. However, if Python finds a module in the module cache, then it won’t bother searching the import path for the module.

### Example: Singletons as Modules

In [object-oriented programming](https://realpython.com/python3-object-oriented-programming/), a **singleton** is a class with at most one instance. While it’s possible to [implement singletons in Python](https://realpython.com/primer-on-python-decorators/#creating-singletons), most good uses of singletons can be handled by modules instead. You can trust the module cache to instantiate a class only once.

As an example, let’s return to the United Nations population data you saw [earlier](https://realpython.com/python-import/#example-use-data-files). The following module defines a class wrapping the population data:

Reading the data from disk takes some time. Since you don’t expect the data file to change, you instantiate the class when you load the module. The name of the class starts with an [underscore](https://realpython.com/python-double-underscore/) to [indicate to users](https://www.python.org/dev/peps/pep-0008/#descriptive-naming-styles) that they shouldn’t use it.

You can use the `population.data` singleton to create a [Matplotlib](https://realpython.com/python-matplotlib-guide/) graph showing the population projection for the most populous countries:

This creates a chart like the following:

[![United Nations population projections](https://files.realpython.com/media/imports-population.fa041527204c.png)](https://files.realpython.com/media/imports-population.fa041527204c.png)

Note that loading the data at import time is a kind of [antipattern](https://en.wikipedia.org/wiki/Anti-pattern). Ideally, you want your imports to be as free of side effects as possible. A better approach would be to load the data lazily when you need it. You can do this quite elegantly using properties. Expand the following section to see an example.

### Reloading Modules

The module cache can be a little frustrating when you’re working in the interactive interpreter. It’s not trivial to reload a module after you change it. For example, take a look at the following module:

As part of testing and [debugging](https://realpython.com/python-debugging-pdb/) this module, you import it in a Python console:

Let’s say you realize that you have a bug in your code, so you update the `number.py` file in your editor:

Returning to your console, you import the updated module to see the effect of your fix:

Why is the answer still `24`? The module cache is doing its (now frustrating) magic: since Python imported `number` earlier, it sees no reason to load the module again even though you just changed it.

The most straightforward solution to this is to exit the Python console and restart it. This forces Python to clear its module cache as well:

However, restarting the interpreter isn’t always feasible. You might be in a more complicated session that has taken you a long time to set up. If that’s the case, then you can use [`importlib.reload()`](https://docs.python.org/library/importlib.html#importlib.reload) to reload a module instead:

Note that `reload()` requires a module object, not a string like `import_module()` does. Also, be aware that `reload()` has some caveats. In particular, variables referring to objects within a module are not re-bound to new objects when that module is reloaded. See [the documentation](https://docs.python.org/library/importlib.html#importlib.reload) for more details.

### Finders and Loaders

You saw [earlier](https://realpython.com/python-import/#pythons-import-path) that creating modules with the same name as standard libraries can create problems. For example, if you have a file named `math.py` in Python’s import path, then you won’t be able to import `math` from the standard library.

This isn’t always the case, though. Create a file named `time.py` with the following content:

Next, open a Python interpreter and import this new module:

Something weird happened. It doesn’t seem like Python imported your new `time` module. Instead, it imported the [`time` module from the standard library](https://realpython.com/python-time-module/). Why are the standard library modules behaving inconsistently? You can get a hint by inspecting the modules:

You can see that `math` is imported from a file, whereas `time` is some kind of built-in module. It seems that built-in modules aren’t shadowed by local ones.

Let’s dig even deeper into Python’s import system. This will also show why built-in modules aren’t shadowed by local ones. There are several steps involved when importing a module:

1.  Python checks if the module is available in the **module cache**. If `sys.modules` contains the name of the module, then the module is already available, and the import process ends.
    
2.  Python starts looking for the module using several **finders**. A finder will search for the module using a given strategy. The default finders can import built-in modules, frozen modules, and modules on the import path.
    
3.  Python loads the module using a **loader**. Which loader Python uses is determined by the finder that located the module and is specified in something called a **module spec**.
    

You can extend the Python import system by implementing your own finder and, if necessary, your own loader. You’ll see a more useful example of a finder later. For now, you’ll learn how to do basic (and possibly silly) customizations of the import system.

`sys.meta_path` controls which finders are called during the import process:

First, note that this answers the question from earlier: built-in modules aren’t shadowed by local modules because the built-in finder is called before the import path finder, which finds local modules. Second, note that you can customize `sys.meta_path` to your liking.

To quickly mess up your Python session, you can remove all finders:

Since there are no finders, Python can’t find or import new modules. However, Python can still import modules that are already in the module cache since it looks there before calling any finders.

In the example above, `importlib` was already loaded under the hood before you cleared the list of finders. If you really want to make your Python session completely unusable, then you can also clear the module cache, `sys.modules`.

The following is a slightly more useful example. You’ll write a finder that prints a message to the console identifying the module being imported. The example shows how to add your own finder, although it doesn’t actually attempt to find a module:

All finders must implement a `.find_spec()` [class method](https://realpython.com/instance-class-and-static-methods-demystified/), which should try to find a given module. There are three ways that `.find_spec()` can terminate:

1.  By **returning `None`** if it doesn’t know how to find and load the module
2.  By **returning a module spec** specifying how to load the module
3.  By **raising a `ModuleNotFoundError`** to indicate that the module can’t be imported

The `DebugFinder` prints a message to the console and then explicitly returns [`None`](https://realpython.com/null-in-python/) to indicate that other finders should figure out how to actually import the module.

By inserting `DebugFinder` first in the list of finders, you get a running list of all modules being imported:

You can, for instance, see that importing `csv` triggers the import of several other modules that `csv` depends on. Note that the verbose option to the Python interpreter, `python -v`, gives the same information and much, much more.

For another example, say that you’re on a quest to rid the world of [regular expressions](https://realpython.com/regex-python/). (Now, [why](http://www.ex-parrot.com/~pdw/Mail-RFC822-Address.html) would you want such a thing? Regular expressions are [great](https://xkcd.com/208/)!) You could implement the following finder that bans the [`re` regular expressions module](https://docs.python.org/3/library/re.html#module-re):

Raising a `ModuleNotFoundError` ensures that no finder later in the list of finders will be executed. This effectively stops you from using [regular expressions](https://regex101.com/) in Python:

Even though you’re importing only `csv`, that module is importing `re` behind the scenes, so an error is raised.

### Example: Automatically Install From PyPI

Because the Python import system is already quite powerful and useful, there are many more ways to mess it up than there are to extend it in a useful way. However, the following example can be useful in certain situations.

The [Python Package Index](https://pypi.org/) (PyPI) is your one-stop [cheese shop](https://www.youtube.com/watch?v=Hz1JWzyvv8Ap) for finding third-party modules and packages. It’s also the place from which `pip` downloads packages.

In other _Real Python_ tutorials, you may have seen instructions to use [`python -m pip install`](https://docs.python.org/3/installing/index.html#basic-usage) to install the third-party modules and packages you need for following along with examples. Wouldn’t it be great to have Python automatically install missing modules for you?

The following finder attempts to install modules using `pip`:

Compared to the finders you saw earlier, this one is slightly more complicated. By putting this finder last in the list of finders, you know that if you call `PipFinder`, then the module won’t be found on your system. The job of `.find_spec()` is therefore just to do the `pip install`. If the installation works, then the module spec will be created and returned.

Try to use the [`parse`](https://pypi.org/project/parse/) library without installing it yourself:

Normally, `import parse` would’ve raised a `ModuleNotFoundError`, but in this case `parse` is installed and imported.

While the `PipFinder` seemingly works, there are some challenges with this approach. One major problem is that the import name of a module doesn’t always correspond to its name on PyPI. For example, the [_Real Python_ feed reader](https://pypi.org/project/realpython-reader/) is called `realpython-reader` on PyPI, but the import name is simply `reader`.

Using `PipFinder` to import and install `reader` ends up installing the wrong package:

This could have disastrous consequences for your project.

One situation in which automatic installations can be quite helpful is when you’re running Python in the cloud with more limited control over your environment, such as when you’re running [Jupyter-style notebooks](https://realpython.com/jupyter-notebook-introduction/) at [Google Colaboratory](https://colab.research.google.com/). The Colab notebook environment is great for doing cooperative data exploration.

A typical notebook comes with many data science packages installed, including [NumPy](https://realpython.com/numpy-array-programming/), [Pandas](https://realpython.com/learning-paths/pandas-data-science/), and [Matplotlib](https://realpython.com/python-matplotlib-guide/), and you can [add new packages](https://colab.research.google.com/notebooks/snippets/importing_libraries.ipynb) with `pip`. But you can also activate automatic installation:

[![Automatically installing packages inside Google Colab](https://files.realpython.com/media/imports-colab-pip_importer.9d9fd1760f1b.png)](https://files.realpython.com/media/imports-colab-pip_importer.9d9fd1760f1b.png)

Since `pip_importer` isn’t available locally on the Colab server, the code is copied into the first cell of the notebook.

### Example: Import Data Files

The final example in this section is inspired by Aleksey Bilogur’s great blog post [Import Almost Anything in Python: An Intro to Module Loaders and Finders](https://blog.quiltdata.com/import-almost-anything-in-python-an-intro-to-module-loaders-and-finders-f5e7b15cda47). You’ve [already seen](https://realpython.com/python-import/#introducing-importlibresources) how to use `importlib.resources` to import datafiles. Here, you’ll instead implement a custom loader that can import a CSV file directly.

[Earlier](https://realpython.com/python-import/#example-use-data-files), you worked with a huge CSV file with population data. To make the custom loader example more manageable, consider the following smaller `employees.csv` file:

The first line is a header naming three fields, and the following two rows of data each contain information about an employee. For more information about working with CSV files, check out [Reading and Writing CSV Files in Python](https://realpython.com/python-csv/).

Your goal in this section is to write a finder and a loader that allow you to import the CSV file directly so that you can write code like the following:

The job of the finder will be to search for and recognize CSV files. The loader’s job will be to import the CSV data. Often, you can implement finders and corresponding loaders in one common class. That’s the approach you’ll take here:

There’s quite a bit of code in this example! Luckily, most of the work is done in `.find_spec()` and `.exec_module()`. Let’s look at them in more detail.

As you saw earlier, `.find_spec()` is responsible for finding the module. In this case, you’re looking for CSV files, so you create a filename with a `.csv` suffix. `name` contains the full name of the module that is imported. For example, if you use `from data import employees`, then `name` will be `data.employees`. In this case, the filename will be `employees.csv`.

For top-level imports, `path` will be `None`. In that case, you look for the CSV file in the full import path, which will include the current working directory. If you’re importing a CSV file within a package, then `path` will be set to the path or paths of the package. If you find a matching CSV file, then a module spec is returned. This module spec tells Python to load the module using `CsvImporter`.

The CSV data is loaded by `.exec_module()`. You can use `csv.DictReader` from the standard library to do the actual parsing of the file. Like most things in Python, modules are backed by dictionaries. By adding the CSV data to `module.__dict__`, you make it available as attributes of the module.

For instance, adding `fieldnames` to the module dictionary on **line 44** allows you to list the field names in the CSV file as follows:

In general, CSV field names can contain spaces and other characters that aren’t allowed in Python attribute names. Before adding the fields as attributes on the module, you [sanitize the field names using a regular expression](https://stackoverflow.com/a/3305731). This is done in `_identifier()` starting on **line 51**.

You can see an example of this effect in the `birthday_month` field name above. If you look at the original CSV file, then you’ll see that the header says `birthday month` with a space instead of an underscore.

By hooking this `CsvImporter` into the Python import system, you get a fair bit of functionality for free. For example, the module cache will make sure that the data file is loaded only once.

## Import Tips and Tricks

To round out this tutorial, you’ll see a few tips about how to handle certain situations that come up from time to time. You’ll see how to deal with missing packages, cyclical imports, and even packages stored inside ZIP files.

### Handle Packages Across Python Versions

Sometimes you need to deal with packages that have different names depending on the Python version. You’ve already seen one example of this: [`importlib.resources`](https://realpython.com/python37-new-features/#importing-data-files-with-importlibresources) has only been available since Python 3.7. In earlier versions of Python, you need to install and use [`importlib_resources`](https://pypi.org/project/importlib_resources/) instead.

As long as the different versions of the package are compatible, you can handle this by renaming the package with `as`:

In the rest of the code, you can refer to `resources` and not worry about whether you’re using `importlib.resources` or `importlib_resources`.

Normally, it’s easiest to use a `try...except` statement to figure out which version to use. Another option is to inspect the version of the Python interpreter. However, this may add some maintenance cost if you need to update the version numbers.

You could rewrite the previous example as follows:

This would use `importlib.resources` on Python 3.7 and newer while falling back to `importlib_resources` on older versions of Python. See the [`flake8-2020`](https://pypi.org/project/flake8-2020/) project for good and future-proof advice on how to check which Python version is running.

### Handle Missing Packages: Use an Alternative

The following use case is closely related to the previous example. Assume there’s a compatible reimplementation of a package. The reimplementation is better optimized, so you want to use it if it’s available. However, the original package is more easily available and also delivers acceptable performance.

One such example is [`quicktions`](https://pypi.org/project/quicktions/), which is an optimized version of `fractions` from the standard library. You can handle these preferences the same way you handled different package names earlier:

This will use `quicktions` if it’s available and fall back to `fractions` if not.

Another similar example is the [UltraJSON package](https://pypi.org/project/ujson/), an ultrafast JSON encoder and decoder that can be used as a replacement for [`json`](https://realpython.com/courses/working-json-data-python/) in the standard library:

By renaming `ujson` to `json`, you don’t have to worry about which package was actually imported.

### Handle Missing Packages: Use a Mock Instead

A third, related example is adding a package that provides a nice-to-have feature that’s not strictly necessary for your app. Again, this can be solved by adding `try...except` to your imports. The extra challenge is how you will replace the optional package if it’s not available.

For a concrete example, say that you’re using [Colorama](https://pypi.org/project/colorama/) to add colored text in the console. Colorama mainly consists of special string constants that add color when printed:

Unfortunately, the color doesn’t render in the example above. In your [terminal](https://realpython.com/terminal-commands/) it’ll look something like this:

[![Adding color to the console with colorama](https://files.realpython.com/media/imports-colorama.c97ed952fe16.png)](https://files.realpython.com/media/imports-colorama.c97ed952fe16.png)

Before you start using Colorama colors, you should call `colorama.init()`. Setting `autoreset` to `True` means that the color directives will be automatically reset at the end of the string. It’s a useful setting if you want to color just one line at a time.

If you’d rather have _all_ your output be (for example) blue, then you can let `autoreset` be `False` and add `Fore.BLUE` to the beginning of your script. The following colors are available:

You can also use `colorama.Style` to control the style of your text. You can choose between `DIM`, `NORMAL`, and `BRIGHT`.

Finally, `colorama.Cursor` provides codes for controlling the position of the cursor. You can use it to display the progress or status of a running script. The following example displays a countdown from `10`:

Note how the counter stays in place instead of printing on separate lines as it normally would:

[![Countdown to lift off with colorama](https://files.realpython.com/media/imports-countdown1.c1396d759b30.gif)](https://files.realpython.com/media/imports-countdown1.c1396d759b30.gif)

Let’s get back to the task at hand. For many applications, adding color to your console output is cool but not critical. To avoid adding yet another dependency to your app, you want to use Colorama only if it’s available on the system and not break the app if it isn’t.

To do this, you can take inspiration from [testing](https://realpython.com/python-testing/) and its use of [mocks](https://realpython.com/python-mock-library/). A mock can substitute for another object while allowing you to control its behavior. Here’s a naïve attempt at mocking Colorama:

This doesn’t quite work, because `Fore.RED` is represented by a string that messes up your output. Instead, you want to create an object that always renders as the empty string.

It’s possible to change the return value of `.__str__()` on `Mock` objects. However, in this case, it’s more convenient to write your own mock:

`ColoramaMock("")` is an empty string that will also return the empty string when it’s called. This effectively gives us a reimplementation of Colorama, just without the colors.

The final trick is that `.__getattr__()` returns itself, so that all colors, styles, and cursor movements that are attributes on `Back`, `Fore`, `Style`, and `Cursor` are mocked as well.

The `optional_color` module is designed to be a drop-in replacement for Colorama, so you can update the countdown example using search and replace:

If you run this script on a system in which Colorama isn’t available, then it’ll still work, but it may not look as nice:

[![Countdown to lift off without colorama](https://files.realpython.com/media/imports-countdown2.300d48e9231d.gif)](https://files.realpython.com/media/imports-countdown2.300d48e9231d.gif)

With Colorama installed, you should see the same results as earlier.

### Import Scripts as Modules

One difference between scripts and library modules is that scripts typically do something, whereas libraries provide functionality. Both scripts and libraries live inside regular Python files, and as far as Python is concerned, there’s no difference between them.

Instead, the difference is in how the file is meant to be used: should it be executed with `python file.py` or imported with `import file` inside another script?

Sometimes you’ll have a module that works as both a script and a library. You could try to [refactor](https://realpython.com/python-refactoring/) your module into two different files.

One example of this in the standard library is the [`json` package](https://docs.python.org/library/json.html). You usually use it as a library, but it also comes bundled with a script that can prettify JSON files. Assume you have the following [`colors.json` file](https://www.sitepoint.com/colors-json-example/):

As JSON is often read only by machines, many JSON files aren’t formatted in a readable fashion. In fact, it’s quite common for JSON files to consist of one very long line of text.

`json.tool` is a script that uses the `json` library to format JSON in a more readable fashion:

Now the structure of the JSON file becomes much less complicated to grasp. You can use the `--sort-keys` option to sort keys alphabetically.

While it’s good practice to split scripts and libraries, Python has an idiom that makes it possible to treat a module as both a script and a library at the same time. As [noted earlier](https://realpython.com/python-import/#example-structure-your-imports), the value of the special `__name__` module variable is set at runtime based on whether the module is imported or run as a script.

Let’s test it out! Create the following file:

If you run this file, then you’ll see that `__name__` is set to the special value `__main__`:

However, if you import the module, then `__name__` is set to the name of the module:

This behavior is leveraged in the following pattern:

Let’s use this in a bigger example. In an attempt to [keep you young](https://en.wikipedia.org/wiki/Fountain_of_Youth), the following script will replace any “old” age (`25` or above) with `24`:

You can run this as a script, and it will interactively make the age you type younger:

You can also use the module as an importable library. The `if` test on **line 12** makes sure that there are no side effects when you import the library. Only the functions `make_young()` and `replace_by_age()` are defined. You can, for instance, use this library as follows:

Without the protection of the `if` test, the import would have triggered the interactive `input()` and made `feel_young` very hard to use as a library.

### Run Python Scripts From ZIP Files

A slightly obscure feature of Python is that it can [run scripts packaged into ZIP files](https://www.python.org/dev/peps/pep-0273/). The main advantage of this is that you can distribute a full package as a single file.

Note, however, that this still requires Python to be installed on the system. If you want to distribute your Python application as a stand-alone executable file, then see [Using PyInstaller to Easily Distribute Python Applications](https://realpython.com/pyinstaller-python/).

If you [give the Python interpreter a ZIP file](https://snarky.ca/the-many-ways-to-pass-code-to-python-from-the-terminal/#executing-a-zip-file), then it’ll look for a file named `__main__.py` inside the ZIP archive, extract it, and run it. As a basic example, create the following `__main__.py` file:

This will print a message when you run it:

Now add it to a ZIP archive. You may be able to do this on the command line:

On Windows, you can instead use [point and click](https://support.microsoft.com/en-us/help/14200/windows-compress-uncompress-zip-files). Select the file in the File Explorer, then right-click and select _Send to → Compressed (zipped) folder_.

Since `__main__` isn’t a very descriptive name, you named the ZIP file `hello.zip`. You can now call it directly with Python:

Note that your script is aware that it lives inside `hello.zip`. Furthermore, the root of your ZIP file is added to Python’s import path so that your scripts can import other modules inside the same ZIP file.

Think back to the earlier example in which you [created a quiz based on population data](https://realpython.com/python-import/#example-use-data-files). It’s possible to distribute this whole application as a single ZIP file. `importlib.resources` will make sure the data file is extracted from the ZIP archive when it’s needed.

The app consists of the following files:

```
<span></span><code>population_quiz/
│
├── data/
│   ├── __init__.py
│   └── WPP2019_TotalPopulationBySex.csv
│
└── population_quiz.py
</code>
```

You could add these to a ZIP file in the same way you did above. However, Python comes with a tool called [`zipapp`](https://docs.python.org/library/zipapp.html) that streamlines the process of packing applications into ZIP archives. You use it as follows:

This command essentially does two things: it creates an entry point and packages your application.

Remember that you needed a `__main__.py` file as an entry point inside your ZIP archive. If you supply the `-m` option with information about how your app should be started, then `zipapp` creates this file for you. In this example, the generated `__main__.py` looks like this:

This `__main__.py` is packaged, along with the contents of the `population_quiz` directory, into a ZIP archive named `population_quiz.pyz`. The `.pyz` suffix signals that this is a Python file wrapped into a ZIP archive.

On Windows, `.pyz` files should already be registered as Python files. On Mac and Linux, you can have `zipapp` create executable files by using the `-p` interpreter option and specifying which interpreter to use:

The `-p` option adds a [shebang (`#!`)](https://realpython.com/python-shebang/) that [tells the operating system how to run the file](https://realpython.com/run-python-scripts/#using-the-script-filename). Additionally, it makes the `.pyz` file executable so that you can run the file just by typing its name:

Notice the `./` in front of the filename. This is a typical trick on Mac and Linux to run executable files in the current directory. If you move the file to a directory on your [`PATH`](https://realpython.com/add-python-to-path/), or if you’re using Windows, then you should be able to use only the filename: `population_quiz.pyz`.

Let’s close this section by looking at a nice effect of using `importlib.resources`. Remember that you used the following code to open the data file:

A more common way to open data files is to locate them based on your module’s `__file__` attribute:

This approach usually works well. However, it falls apart when your application is packed into a ZIP file:

Your data file is inside the ZIP archive, so `open()` isn’t able to open it. `importlib.resources`, on the other hand, will extract your data to a temporary file before opening it.

### Handle Cyclical Imports

A cyclical import happens when you have two or more modules importing each other. More concretely, imagine that the module `yin` uses `import yang` and the module `yang` similarly imports `yin`.

[![An example of a cyclical import](https://files.realpython.com/media/imports-cyclical.4ab1975c7073.png)](https://files.realpython.com/media/imports-cyclical.4ab1975c7073.png)

Python’s import system is to some extent designed to handle import cycles. For instance, the following code—while not very useful—runs fine:

Trying to import `yin` in the interactive interpreter imports `yang` as well:

Note that `yang` is imported in the middle of the import of `yin`, precisely at the `import yang` statement in the source code of `yin`. The reason this doesn’t end up in endless [recursion](https://realpython.com/python-recursion/) is our old friend the module cache.

When you type `import yin`, a reference to `yin` is added to the module cache even before `yin` is loaded. When `yang` tries to import `yin` later, it simply uses the reference in the module cache.

You can also have modules that do something slightly more useful. If you define attributes and functions in your modules, then it all still works:

Importing `yin` works the same as before:

The issues associated with recursive imports start popping up when you actually use the other module at import time instead of just defining functions that will use the other module later. Add one line to `yang.py`:

Now Python gets confused by the import:

The error message may seem a bit puzzling at first. Looking back at the source code, you can confirm that `number` is defined in the `yin` module.

The problem is that `number` isn’t defined in `yin` at the time `yang` gets imported. Consequently, `yin.number` is used by the call to `combine()`.

To add to the confusion, you’ll have no issues importing `yang`:

By the time `yang` calls `combine()`, `yin` is fully imported and `yin.number` is well defined. As a final twist, because of the module cache you saw earlier, `import yin` might work if you do some other imports first:

So how can you avoid being bogged down and confused by cyclical imports? Having two or more modules importing each other is often a sign that you can improve the design of your modules.

Often, the easiest time to fix cyclical imports is _before_ you implement them. If you see cycles in your architecture sketches, have a closer look and **try to break the cycles**.

Still, there are times when it’s reasonable to introduce an import cycle. As you saw above, this isn’t a problem so long as your modules define only attributes, functions, classes, and so on. The second tip—which is also good design practice—is to **keep your modules free of side effects at import time**.

If you really need modules with import cycles and side effects, there’s still another way out: **do your imports locally inside functions**.

Note that in the following code, `import yang` is done inside `combine()`. This has two consequences. First, `yang` is available only inside the `combine()` function. More importantly, the import doesn’t happen until you call `combine()` after `yin` has been fully imported:

Now there are no issues importing and using `yin`:

Notice that `yang` is, in fact, not imported until you call `combine()`. For another perspective on cyclical imports, see [Fredrik Lundh’s classic note](https://effbot.org/zone/import-confusion.htm#circular-imports).

### Profile Imports

One concern when importing several modules and packages is that it will add to the startup time of your script. Depending on your application, this may or may not be critical.

Since the release of [Python 3.7](https://realpython.com/python37-new-features/#developer-tricks), you’ve had a quick way of knowing how much time it takes to import packages and modules. Python 3.7 supports the `-X importtime` command-line option, which measures and prints how much time each module takes to import:

The `cumulative` column shows the cumulative time of import (in microseconds) on a per-package basis. You can read the listing as follows: Python spent `1320` microseconds to fully import `datetime`, which involved importing `time`, `math`, and the C implementation `_datetime` as well.

The `self` column shows the time it took to import only the given module, excluding any recursive imports. You can see that `time` took `87` microseconds to import, `math` took `180`, `_datetime` took `234`, and the import of `datetime` itself took `820` microseconds. All in all, this adds up to a cumulative time of `1320` microseconds (within rounding errors).

Have a look at the `countdown.py` example from the [Colorama section](https://realpython.com/python-import/#handle-missing-packages-use-a-mock-instead):

In this example, importing `optional_color` took almost 0.013 seconds. Most of that time was spent importing Colorama and its dependencies. The `self` column shows the import time excluding nested imports.

For an extreme example, consider the [`population` singleton from earlier](https://realpython.com/python-import/#example-singletons-as-modules). Because it’s loading a big data file, it’s extremely slow to import. To test this, you can run `import population` as a script with the `-c` option:

In this case, it takes almost 2 seconds to import `population`, of which about 1.6 seconds are spent in the module itself, mainly for loading the data file.

`-X importtime` is a great tool for optimizing your imports. If you need to do more general monitoring and optimization of your code, then check out [Python Timer Functions: Three Ways to Monitor Your Code](https://realpython.com/python-timer/).

## Conclusion

In this tutorial, you’ve gotten to know the Python import system. Like many things in Python, it’s fairly straightforward to use for basic tasks like importing modules and packages. At the same time, the import system is quite complex, flexible, and extendable. You’ve learned several import-related tricks that you can take advantage of in your own code.

**In this tutorial, you’ve learned how to:**

-   Create **namespace packages**
-   Import **resources** and **data files**
-   Decide what to import **dynamically** at runtime
-   **Extend** Python’s import system
-   Handle different **versions** of packages

Throughout the tutorial, you’ve seen many links to further info. The most authoritative source on the Python import system is the official documentation:

-   [The import system](https://docs.python.org/reference/import.html)
-   [The `importlib` package](https://docs.python.org/library/importlib.html)
-   [PEP 420: Implicit namespace packages](https://www.python.org/dev/peps/pep-0420/)
-   [Importing modules](https://docs.python.org/library/modules.html)

You can put your knowledge of Python imports to use by following along with the examples in this tutorial. Click the link below for access to the source code:

Watch Now This tutorial has a related video course created by the Real Python team. Watch it together with the written tutorial to deepen your understanding: [**Advanced Python import Techniques**](https://realpython.com/courses/advanced-import-techniques/)