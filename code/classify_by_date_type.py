import os
import time
import shutil

import optparse


def get_all_files(rootpath):
    files = os.listdir(rootpath)
    paths = [os.path.join(rootpath, f) for f in files if not f.endswith('py')]
    return paths

def make_dirs(outpath, dates, types):
    for d in dates:
        dpath = os.path.join(outpath, d)
        if not os.path.exists(dpath):
            os.mkdir(dpath)
        for t in types:
            tpath = os.path.join(dpath, t)
            if not os.path.exists(tpath):
                os.mkdir(tpath)

def parse_cmd():
    parse=optparse.OptionParser(usage='"usage:%prog [options] arg1,arg2"',version="%prog 1.2")  
    parse.add_option('-i','--inpath',dest='inpath',type=str,default='.',help='Enter Inpath!!')
    parse.add_option('-o','--outpath',dest='outpath',type=str,default='.',help='Enter Root Outpath!!')
    parse.add_option('-g','--greater',dest='gdate',type=str,default='0000-00-00',help='Entete Date YYYY-mm-dd to remain greater file!!')  
    options,args=parse.parse_args() 
    return options

def filt_by_time(paths, gdate):
    anspaths = []
    for p in paths:
        mtime = os.path.getmtime(p)
        mtime_str = time.strftime("%Y-%m-%d", time.localtime(mtime))
        if mtime_str > gdate:
            anspaths.append(p)
    return anspaths

# E:/Anaconda/envs/py3/python.exe classify_by_data_type.py -i I:\DCIM\100MEDIA -o H:\航拍素材
if __name__ == '__main__':
    op = parse_cmd()
    inpath = op.inpath
    outpath = op.outpath
    gdate = op.gdate
    filepaths = get_all_files(inpath)
    # 按时间过滤文件
    filepaths = filt_by_time(filepaths, gdate)
    suffixs = [os.path.splitext(p)[-1][1:] for p in filepaths]
    mtimes = [os.path.getmtime(p) for p in filepaths]
    mtimestrs = [time.strftime("%Y-%m-%d", time.localtime(t)) for t in mtimes]
    dates = set(mtimestrs)
    types = set(suffixs)        
    make_dirs(outpath, dates, types)
    total = len(filepaths)
    print('need copy date:', sorted(dates), 'total:', total)
    i = 1
    for filepath,filetype,date in zip(filepaths, suffixs, mtimestrs):
        # 如果文件修改日期不晚于指定日期，则不做复制。也就是文件修改日期晚于指定日期，才会做出修改。
        dst_dir = os.path.join(outpath, date, filetype)
        dirpath, filename = os.path.split(filepath)
        outfile = os.path.join(dst_dir, filename)
        shutil.copyfile(filepath, outfile)
        print("finish copy file:", os.path.abspath(filepath), "to", os.path.abspath(outfile),"--> %s/%s"%(i, total))
        i += 1