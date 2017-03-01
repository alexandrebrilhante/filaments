import numpy
import mahotas as mh

distances = [.185, .04, .04]


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
    flen = 0
    skel_cube = skel[(pos[2]-1):(pos[2]+2),
                     (pos[1]-1):(pos[1]+2),
                     (pos[0]-1):(pos[0]+2)]
    stop = False
    prev = [0, 0, 0]
    while(len(skel_cube) > 0 and sum(sum(sum(skel_cube))) < 4 and not stop):
        n += 1
        npos = numpy.where(skel_cube > 0)
        found = False
        for ii in xrange(len(npos[0])):
            step = [npos[2][ii] - 1, npos[1][ii] - 1, npos[0][ii] - 1]
            if(sum(numpy.add(step, prev)) != 0 and sum(step) != 0):
                pos = numpy.add(pos, step)
                flen += sum(abs(numpy.multiply(distances, step)))
                found = True
                skel_cube = skel[(pos[2]-1):(pos[2]+2),
                                 (pos[1]-1):(pos[1]+2),
                                 (pos[0]-1):(pos[0]+2)]
                if(len(skel_cube) == 0):
                    found = False
                prev = step
                break
        stop = not found
    pos = numpy.add(pos, prev)
    return({'n': n, 'branch': pos, 'length': flen})


def travelSkel(skel):
    ep = endPoints(skel)
    ep = numpy.where(ep > 0)
    fils = []
    for ii in xrange(len(ep[0])):
        fil = {'z': ep[0][ii], 'y': ep[1][ii], 'x': ep[2][ii]}
        ffil = followFil(skel, fil)
        fil['n'] = ffil['n']
        fil['branch'] = ffil['branch']
        fil['length'] = ffil['length']
        fils.append(fil)
    return(fils)


def pruning(skeleton, size):
    for i in range(0, size):
        endpoints = endPoints(skeleton)
        endpoints = numpy.logical_not(endpoints)
        skeleton = numpy.logical_and(skeleton, endpoints)
    return skeleton


def pruneFil(skel, fil):
    pos = [fil['x'], fil['y'], fil['z']]
    skel_cube = skel[(pos[2]-1):(pos[2]+2),
                     (pos[1]-1):(pos[1]+2),
                     (pos[0]-1):(pos[0]+2)]
    branch = fil['branch']
    step = [0, 0, 0]
    while(len(skel_cube) > 0 and sum(sum(sum(skel_cube != 0))) > 0 and
          pos[2] < len(skel) and
          pos[1] < len(skel[0]) and pos[0] < len(skel[0][0])):
        stop = False
        skel[pos[2], pos[1], pos[0]] = 0
        npos = numpy.where(skel_cube > 0)
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

# sk = numpy.zeros((300, 300, 300), dtype=numpy.uint8)
# sk[2:280, 150, 150] = 1
# sk[150, 2:280, 150] = 1
# sk[200, 150, 3:200] = 1
# sk

# fils = travelSkel(sk)
# skp = pruning(sk, 4)
# skp = pruneFil(sk, fils[5])

# fils2 = travelSkel(skp)
# ep = endPoints(sk)
