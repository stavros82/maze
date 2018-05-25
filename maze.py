
# coding: utf-8

# In[1]:


import sys,os,argparse
from IPython.display import HTML
CONFIG_FILE = '.config_ipynb'
#if os.path.isfile(CONFIG_FILE):
#    with open(CONFIG_FILE) as f:
#        sys.argv = f.read().split()
#else:
#    sys.argv = ['input_path','C:\\Users\\Stavros\\Desktop\\maze\\small.txt']

parser = argparse.ArgumentParser()

parser.add_argument("input_path", type=str,  help="an optional integer parameter.")
args = parser.parse_args()



# # The input file

# In[2]:


import numpy as np

f = open(args.input_path, encoding='utf-8') 
mylist = [line.rstrip('\n')  for line in f]


# In[6]:


data = mylist[3:]


l=[]
for item in data:
    subl = []
    for num in item.split(' '):
        subl.append(str(num))
    l.append(subl)

matrix=np.array(l)

start=[]
for num in mylist[1].split(' '):
       start.append(num)
end=[]        
for num in mylist[2].split(' '):
       end.append(num)        
matrix=np.where(matrix == '1','#', matrix)


#start=mylist[1]
#end=mylist[2]



matrix[int(start[0]),int(start[1])]='S'
matrix[int(end[0]),int(end[1])]='E'

print('The input file')
print(matrix)




# # The out put file

# In[4]:





x=int(start[0])
y=int(start[1])


validDirection={}
path=[]
while True:
   validDirection.clear() 
   
   south=matrix[int(x)+1,int(y)]
   north=matrix[int(x)-1,int(y)]
   west=matrix[int(x),int(y)-1]
   east=matrix[int(x),int(y)+1]
   
   if (south=='E' or north=='E' or west=='E' or east=='E'):
        break
   
   if (south!='0' and north!='0' and west!='0' and east!='0'):
        matrix[int(x),int(y)] ='d'
        #remove the last one
        path = path[:-1]
        matrix=np.where(matrix == 'x','0', matrix)
        x=int(start[0])
        y=int(start[1])
        path.clear()
   
      
   if east=='0':  
         validDirection[str(x)+' '+str(y)]=str(int(x))+' '+str(int(y)+1)
    
   if north=='0':
          validDirection[str(x)+' '+str(y)]=str(int(x)-1)+' '+str(int(y)) 
    
   if south=='0':
          validDirection[str(x)+' '+str(y)]=str(int(x)+1)+' '+str(int(y))
   if west =='0':
          validDirection[str(x)+' '+str(y)]=str(int(x))+' '+str(int(y)-1)      
   
  
   if len(validDirection)!=0:    
        for key in validDirection:
            i = validDirection[key].split(' ')
            x=i[0]
            y=i[1]
            path.append(x+' '+y) 
            matrix[int(x),int(y)] ='x'
            break


matrix=np.where(matrix == 'd','0', matrix)
print('The output file')
print(matrix)

   


# In[ ]:




