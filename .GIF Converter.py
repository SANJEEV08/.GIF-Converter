#Importing packages
import imageio                  #Image Wrapper for python
import os                       #Performing system related operations

                   
clip=os.path.abspath("3.mp4")   #Input variable containing the video



#Function definition
def gifmaker(inputsource,targetformat):  
    
    #Name of the gif's file that will be created 
    outputpath=os.path.splitext(inputsource)[0]+targetformat
    
    #A reader variable that reads in the input clip provided
    reader=imageio.get_reader(inputsource)
    
    #A fps variable to find the frames per second of the original video clip
    fps=reader.get_meta_data()["fps"]
    
    #A writer variable to write into the Output with same number of frames per second as the original
    writer=imageio.get_writer(outputpath,fps=fps)
    
    #Looping to write every frame of input to the output
    for frames in reader:
        writer.append_data(frames)
   
    
    #Writer function closed
    writer.close()



#Function call to execute
gifmaker(clip,".gif")