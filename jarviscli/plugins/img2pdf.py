from plugin import plugin
import img2pdf


@plugin("img2pdf")
def image2pdf(jarvis,s):
    
    """Converts png file from path to pdf, the output file is 
       in the same folder as the input file.
       Your file must be in the Jarvis folder.
    """




    if not s:
        jarvis.say("please enter file path after calling the plugin")
    elif (not "png" in s ) and (not "jpeg" in s):
        jarvis.say("Your file must be a .png or a .jpeg file")
    else:
        #We have to add the '.' back beacause the Jarvis API removes it
        if "png" in s:
            s = s.replace('png', '.' + 'png')
            source_path=s
            dest_path= s.replace('.png', '') + '.pdf'       
        elif "jpeg" in s:
            s = s.replace('jpeg', '.' + 'jpeg')
            source_path=s
            dest_path= s.replace('.jpeg', '') + '.pdf'       
            
        try:   
            pdf_bytes = img2pdf.convert(source_path)
            file = open(dest_path, "wb")
            file.write(pdf_bytes)
            file.close()
            jarvis.say("file successfully converted")
        except:
            jarvis.say("Something went wrong, images with alpha channels are not supported")
