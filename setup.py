
# coding: utf-8

# In[1]:


from cx_Freeze import setup, Executable

base = None    

executables = [Executable("Sampling Creator.py", base=base)]

packages = ["idna"]
options = {
    'build_exe': {    
        'packages':packages,
    },    
}

setup(
    name = "Sampling Creator",
    options = options,
    version = "0.2",
    description = 'This is a graphical editor for replenishing the sample',
    executables = executables
)

