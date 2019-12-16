from plugin import plugin
import img2pdf


@plugin("img2pdf")
def image2pdf(jarvis,s):
    
    """Converts png file from path to pdf, the output file is 
       in the same folder as the input file.
       Your file must be in the Jarvis folder.
    """



    jarvis.say("Enter file name (with the .png/.jpeg extension), the file must be in the Jarvis folder")
    source_path = jarvis.input()
    if not source_path:
        jarvis.say("please enter file path after calling the plugin")
    elif (not "png" in source_path ) and (not "jpeg" in source_path):
        jarvis.say("Your file must be a .png or a .jpeg file")
    else:
        #We have to add the '.' back beacause the Jarvis API removes it
        if "png" in source_path:
            
            dest_path= source_path.replace('.png', '') + '.pdf'       
        elif "jpeg" in source_path:
            
            dest_path= source_path.replace('.jpeg', '') + '.pdf'       
            
        try:   
            pdf_bytes = img2pdf.convert(source_path)
            file = open(dest_path, "wb")
            file.write(pdf_bytes)
            file.close()
            jarvis.say("file successfully converted")
        except:
            jarvis.say("Something went wrong, images with alpha channels are not supported")
