
# coding: utf-8

# In[1]:


from configparser import ConfigParser
def read_db_config(filename="conf.ini",section="MYSQL"):
    parser=ConfigParser()
    parser.read(filename)
    db={}
    if parser.has_section(section):
        items=parser.items(section)
        for item in items:
            db[item[0]]=item[1]
    else:
        raise Exception("{}section not found in {}.format(section,filename)")
    return db
#r=read_db_config()
#print(r)

