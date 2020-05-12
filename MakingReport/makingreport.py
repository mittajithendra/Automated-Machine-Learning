from PIL import Image
import os
def report():
    images_list=[]
    k=0
    pat=os.path.join(os.getcwd(),'FinalReport')
    
    for i in os.listdir(pat):
        if k==0:
            im1=os.path.join(os.getcwd(),'FinalReport',i)
            im1=Image.open(im1)
            im1=im1.convert('RGB')
        else:
            images_list.append(Image.open(os.path.join(os.getcwd(),'FinalReport',i)).convert('RGB'))
        k+=1
    if k==1:
        im1.save(r'./myReport.pdf',save_all=True)
    else:
        im1.save(r'./myReport.pdf',save_all=True, append_images=images_list)
