# -*- coding: utf-8 -*-
# @Author: lucky
# @Date:   2018-08-19 21:39:51
# @Last Modified by:   zxy987872674
# @Last Modified time: 2018-08-19 22:25:39
# 获取经度和纬度

from pygeocoder import Geocoder

if __name__ == '__main__':
    address = '207 N. Defiance St,Archbold, OH'
    print(Geocoder.geocode(address)[0].coordinates)
