from lstm1119 import *


if __name__ == "__main__":
    netw = Predictor()
    viz = Grapher()

    qwe = {0: [[572.4468994140625, 290.0390625], [572.4468994140625, 290.0390625], [572.4468994140625, 290.0390625], [578.4515991210938, 295.71014404296875], [583.7890625, 300.046875], [591.4617309570312, 307.552734375], [596.4656372070312, 311.3890686035156], [603.1375122070312, 319.06170654296875], [610.4765625, 327.40155029296875], [619.1500244140625, 335.07421875], [625.8218994140625, 343.7476806640625], [637.4976806640625, 354.42266845703125]], 1: [[687.8703002929688, 325.73358154296875], [687.8703002929688, 325.73358154296875], [687.8703002929688, 325.73358154296875], [698.5453491210938, 331.73828125], [709.2203369140625, 339.07733154296875], [720.5625, 348.7515869140625], [731.9047241210938, 357.0914306640625], [745.2484741210938, 367.4328308105469], [759.9265747070312, 375.7726745605469], [760.59375, 375.4390869140625], [775.2719116210938, 387.78204345703125], [792.6187744140625, 398.12347412109375], [792.6187744140625, 397.1226806640625], [812.6343994140625, 412.1343994140625]], 2: [[252.36367797851562, 274.36016845703125], [252.36367797851562, 274.36016845703125], [252.36367797851562, 274.36016845703125], [253.3644561767578, 273.6929626464844], [255.3660125732422, 273.19256591796875], [257.5343933105469, 271.69140625], [258.8687438964844, 270.0234375], [260.8703308105469, 268.8558654785156], [262.03790283203125, 268.6890563964844], [264.7066345214844, 266.6875], [300.7347717285156, 213.81289672851562], [335.42852783203125, 214.8136749267578], [365.6187438964844, 191.7957000732422], [360.28125, 234.99609375], [379.9632873535156, 205.806640625], [336.095703125, 214.146484375], [301.90234375, 213.4792938232422], [365.28515625, 189.9609375], [360.6148376464844, 234.49569702148438], [380.296875, 205.6398468017578], [336.5960998535156, 213.1457061767578]], 3: [[357.2789001464844, 242.3351593017578], [379.62969970703125, 207.97500610351562], [331.7590026855469, 218.1496124267578], [344.9359436035156, 205.1394500732422], [362.6164245605469, 193.63046264648438], [357.2789001464844, 242.3351593017578], [379.62969970703125, 207.97500610351562], [331.7590026855469, 218.1496124267578], [344.9359436035156, 205.1394500732422], [362.6164245605469, 193.63046264648438], [357.2789001464844, 242.3351593017578], [379.62969970703125, 207.97500610351562], [331.7590026855469, 218.1496124267578], [344.9359436035156, 205.1394500732422], [362.6164245605469, 193.63046264648438], [357.6125183105469, 242.00155639648438], [380.296875, 207.97500610351562], [331.7590026855469, 218.31640625], [297.2320251464844, 216.14804077148438], [344.9359436035156, 204.47225952148438], [358.2796936035156, 241.16757202148438], [379.9632873535156, 207.474609375], [332.09259033203125, 217.3156280517578], [297.3988342285156, 215.48086547851562], [244.02383422851562, 200.6359405517578], [244.02383422851562, 200.46914672851562], [297.5656433105469, 213.64608764648438], [244.1906280517578, 200.46914672851562]], 4: [[491.38360595703125, 267.68829345703125], [491.38360595703125, 267.68829345703125], [491.38360595703125, 267.68829345703125], [493.3851623535156, 272.69219970703125], [496.0539245605469, 275.861328125], [498.72265625, 275.861328125], [501.0578308105469, 285.3687438964844], [502.3921813964844, 288.8714904785156], [505.39453125, 293.8753967285156], [509.0640563964844, 298.7124938964844], [512.06640625, 303.7164001464844], [515.0687866210938, 308.7203063964844]], 5: [[197.15391540527344, 446.16094970703125], [197.15391540527344, 446.16094970703125], [197.15391540527344, 446.16094970703125], [201.1570281982422, 438.15472412109375], [196.1531219482422, 431.14923095703125], [198.15469360351562, 425.4781494140625], [206.32774353027344, 417.80548095703125], [211.9988250732422, 411.46722412109375], [218.50390625, 404.79534912109375], [223.17422485351562, 399.45782470703125], [227.677734375, 392.78594970703125], [232.5148468017578, 387.1148681640625]], 6: [[134.1046905517578, 292.37420654296875], [134.1046905517578, 292.37420654296875], [134.1046905517578, 292.37420654296875], [137.69082641601562, 290.873046875], [141.77734375, 289.37188720703125], [146.28086853027344, 287.2035217285156], [149.7001953125, 285.03515625], [152.3689422607422, 283.7007751464844], [156.6222686767578, 281.3656311035156], [159.9582061767578, 279.86444091796875], [163.0439453125, 279.5308532714844], [165.962890625, 278.0296936035156]], 7: [[451.6859436035156, 203.3046875], [501.39141845703125, 179.7863311767578], [444.68048095703125, 182.6218719482422], [451.6859436035156, 203.4714813232422], [501.39141845703125, 179.7863311767578], [444.68048095703125, 182.6218719482422], [451.6859436035156, 203.3046875], [501.39141845703125, 179.7863311767578], [444.68048095703125, 182.6218719482422], [452.6867370605469, 203.9718780517578], [503.7265625, 181.12069702148438], [507.7297058105469, 182.2882843017578], [453.6875, 206.640625], [443.6796875, 182.95547485351562], [454.0210876464844, 206.30703735351562], [507.0625, 182.6218719482422], [505.7281188964844, 182.12149047851562], [504.72735595703125, 183.2890625], [454.0210876464844, 206.97421264648438], [444.3468933105469, 183.78945922851562], [455.0218811035156, 207.97500610351562], [505.7281188964844, 183.62265014648438], [455.0218811035156, 208.64218139648438], [506.0617370605469, 183.62265014648438], [504.72735595703125, 183.2890625], [455.35546875, 208.64218139648438], [506.7289123535156, 183.62265014648438], [507.0625, 183.78945922851562], [456.0226745605469, 209.142578125], [508.06329345703125, 183.62265014648438], [507.7297058105469, 183.4558563232422], [456.0226745605469, 209.8097686767578], [508.73046875, 183.4558563232422], [508.73046875, 183.1222686767578]], 8: [[295.7308654785156, 217.14883422851562], [244.1906280517578, 200.802734375], [295.7308654785156, 217.14883422851562], [244.1906280517578, 200.802734375], [295.7308654785156, 217.14883422851562], [244.1906280517578, 200.802734375], [244.1906280517578, 200.802734375]], 9: [[653.1765747070312, 131.24842834472656], [654.1773681640625, 131.24842834472656], [653.84375, 131.24842834472656], [653.84375, 131.08163452148438], [654.1773681640625, 131.49862670898438], [653.84375, 131.4152374267578], [653.1765747070312, 130.9148406982422], [657.1796875, 131.66542053222656], [657.5133056640625, 131.58203125], [657.5133056640625, 132.91639709472656], [657.1796875, 132.9998016357422], [657.8468627929688, 131.7488250732422]], 10: [[362.95001220703125, 192.96328735351562]], 11: [[443.6796875, 182.2882843017578]], 12: [[358.2796936035156, 239.8332061767578], [379.62969970703125, 207.14102172851562], [333.2601623535156, 216.8152313232422], [363.9507751464844, 192.96328735351562], [358.61328125, 238.33203125], [379.62969970703125, 206.97421264648438], [333.9273376464844, 216.14804077148438], [298.2328186035156, 213.4792938232422], [364.61798095703125, 192.79647827148438], [358.9468688964844, 236.8308563232422], [379.9632873535156, 206.640625], [334.427734375, 215.9812469482422], [299.0668029785156, 213.4792938232422], [244.1906280517578, 200.6359405517578], [299.9007873535156, 213.64608764648438], [244.1906280517578, 200.6359405517578], [244.357421875, 200.6359405517578], [244.357421875, 200.30233764648438], [244.1906280517578, 200.46914672851562]], 13: [[444.0132751464844, 183.4558563232422]], 14: [[363.9507751464844, 191.96249389648438], [359.9476623535156, 236.4972686767578], [380.296875, 206.640625], [334.9281311035156, 214.98046875], [364.9515686035156, 192.2960968017578], [360.28125, 235.830078125], [379.9632873535156, 206.4738311767578]], 15: [[444.0132751464844, 184.123046875], [445.6812438964844, 185.29061889648438], [445.6812438964844, 185.45742797851562], [447.3492126464844, 186.4582061767578], [447.015625, 186.625]], 16: [[266.20782470703125, 265.853515625], [267.3753967285156, 264.85272216796875], [302.90313720703125, 212.81210327148438], [365.6187438964844, 189.46054077148438]]}
    for i in qwe:
        print(i,qwe[i])
        viz.addDict(i,qwe[i])
    viz.displayFromDict()
 #   plt.plot(qwe)
 #   plt.legend()
 #   plt.show()