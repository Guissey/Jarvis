from plugin import plugin
from pdf2jpg import pdf2jpg


@plugin("pdf2img")
class pdf2img:
    
    """converts pdf file from path to png, the output folder 
       is in the same folder as the input file.
       Your file must be in the Jarvis Folder
    """

    def __call__(self, jarvis, s):

        jarvis.say("Enter file name (with the .pdf extension), the file must be in the Jarvis folder")
        source_path = jarvis.input()
        if not source_path:
            jarvis.say("please enter file path after calling the plugin")
        if not "pdf" in source_path:
            jarvis.say("Your file must be a .pdf file")
        else:
            #We have to add the '.' back beacause the Jarvis API removes it
            s = s.replace('pdf', '.' + 'pdf')
            
            
            dest_path= source_path.replace('.pdf', '')
            jarvis.say(source_path)
            jarvis.say(dest_path)
            result = pdf2jpg.convert_pdf2jpg(source_path, dest_path, pages="ALL")
            jarvis.say("file successfully converted")
