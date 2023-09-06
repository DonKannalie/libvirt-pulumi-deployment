import os
import importlib

def module_iterator(submodule: str, blacklist: list[str] = [], rel_prefix: str = '.'):
    submodule_ls = map(lambda filename: filename[:-3],
                    filter(lambda filename: filename != '__init__.py' and
                                            filename != '__pycache__' and
                                            filename[:-3] not in blacklist,
                        os.listdir(submodule)
                    )
                )

    for file in submodule_ls:
        current_mod = importlib.import_module(f'{rel_prefix}{file}', submodule)
        yield current_mod