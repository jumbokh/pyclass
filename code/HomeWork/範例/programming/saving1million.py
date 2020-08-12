# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 10:15:40 2015

@author: user
"""
sumsave=0
mpv=10000
ypv=120000
r=0.02
target=1000000
#月複利
def monthlysaving(mpv,r,target):
    fv=0
    n=0
    while fv<target:
        fv=(mpv+fv)*(1+r/12)
        n=n+1
    return(n/12,fv)
#年複利
def yearlysaving(ypv,r,target):
    fv=0
    n=0
    while fv<target:
        fv=(ypv+fv)*(1+r)
        n=n+1
    return (n,fv)    
my,msave=monthlysaving(mpv,r,target)
yy,ysave=yearlysaving(ypv,r,target)
print('%s = %.2f %s, %.2f' %('Monthly saving 10000 due to 1 million needs', my, 'years', msave))
print('%s = %d %s, %.2f' %('Yearly saving 120000 due to 1 million needs', yy, 'years', ysave))