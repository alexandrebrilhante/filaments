import numpy
import mahotas as mh


def endPoints(skel):
    zcube = numpy.zeros((3, 3, 3), dtype=numpy.uint8)
    zcube[1, 1, 1] = 1
    ep = numpy.zeros(skel.shape, dtype=numpy.uint8)
    for x in range(3):
        for y in range(3):
            for z in range(3):
                if(z != 1 or x != 1 or y != 1):
                    zcube[z, y, x] = 1
                    ep_xyz = mh.morph.hitmiss(skel, zcube)
                    ep += ep_xyz
                    zcube[z, y, x] = 0
    return ep


def followFil(skel, pos):
    pos = [pos['x'], pos['y'], pos['z']]
    n = 0
    skel_cube = skel[(pos[2]-1):(pos[2]+2),
                     (pos[1]-1):(pos[1]+2),
                     (pos[0]-1):(pos[0]+2)]
    stop = False
    prev = [0, 0, 0]
    while(sum(sum(sum(skel_cube))) < 4 and not stop):
        n += 1
        npos = numpy.where(skel_cube == 1)
        found = False
        for ii in xrange(len(npos[0])):
            step = [npos[2][ii] - 1, npos[1][ii] - 1, npos[0][ii] - 1]
            if(sum(numpy.add(step, prev)) != 0 and sum(step) != 0):
                pos = numpy.add(pos, step)
                found = True
                skel_cube = skel[(pos[2]-1):(pos[2]+2),
                                 (pos[1]-1):(pos[1]+2),
                                 (pos[0]-1):(pos[0]+2)]
                prev = step
                break
        stop = not found
    pos = numpy.add(pos, prev)
    return({'n': n, 'branch': pos})


def travelSkel(skel):
    ep = endPoints(sk)
    ep = numpy.where(ep == 1)
    fils = []
    for ii in xrange(len(ep[0])):
        fil = {'z': ep[0][ii], 'y': ep[1][ii], 'x': ep[2][ii]}
        ffil = followFil(sk, fil)
        fil['n'] = ffil['n']
        fil['branch'] = ffil['branch']
        fils.append(fil)
    return(fils)


def pruneFil(skel, fil):
    pos = [fil['x'], fil['y'], fil['z']]
    skel_cube = skel[(pos[2]-1):(pos[2]+2),
                     (pos[1]-1):(pos[1]+2),
                     (pos[0]-1):(pos[0]+2)]
    branch = fil['branch']
    while(True):
        stop = False
        skel[pos[2], pos[1], pos[0]] = 0
        npos = numpy.where(skel_cube == 1)
        for ii in xrange(len(npos[0])):
            step = [npos[2][ii] - 1, npos[1][ii] - 1, npos[0][ii] - 1]
            nnpos = numpy.add(pos, step)
            if(sum(nnpos == branch) == 3):
                stop = True
        if(stop):
            break
        else:
            pos = numpy.add(pos, step)
            skel_cube = skel[(pos[2]-1):(pos[2]+2),
                             (pos[1]-1):(pos[1]+2),
                             (pos[0]-1):(pos[0]+2)]
    return(skel)

# sk = numpy.zeros((30, 30, 30), dtype=numpy.uint8)
# sk[2:28, 15, 15] = 1
# sk[15, 2:28, 15] = 1
# sk[20, 15, 3:20] = 1
# sk

# fils = travelSkel(sk)
# skp = pruneFil(sk, fils[5])

# fils2 = travelSkel(skp)
