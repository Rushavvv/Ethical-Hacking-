'''A program needs to use a stack data structure. The stack can store up to 10 integer elements.
A 1D array StackData is used to store the stack globally. The global variable StackPointer
points to the next available space in the stack and is initialised to 0.'''

# global stack_data  
# global stack_pointer

stack_data = [0,0,0,0,0,0,0,0,0,0,0]
stack_pointer = 0 
def push(*data): 
    
    global stack_pointer
    global stack_data
    
    if stack_pointer == 11:
        
        return False 
    else:
        stack_data[stack_pointer] = data 
        stack_pointer =+ 1 
        
        return True 

def PrintArray():
 global stack_data
 global stack_pointer
 print(stack_pointer)
 for x in range (0, 11):
   print(stack_data[x])

print(PrintArray())



for x in range (0,11): 
    number = int(input("Enter a number"))
    if push(number) == True: 
        print ("Value stored")
    else: 
        print("Value not stored, Stack full") 
PrintArray() 





'''output = [f"stack data: {stack_data} and stack pointer: {stack_pointer}"]
print(output) '''




        
    
    

push (2)
print(stack_data)


         
