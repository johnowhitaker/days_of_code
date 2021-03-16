# AUTOGENERATED! DO NOT EDIT! File to edit: 02_Meeting_Mice.ipynb (unless otherwise specified).

__all__ = ['draw_instant', 'augment_sequence']

# Cell
def draw_instant(ctx, seq, w, h, T, n=30, step=3):
    """ Draw the two mice with fainter 'trails' of shapes showing their past and future movement"""
    imw, imh = 1024, 570
    for i in range(T-n, T+n, step):
        for mouse in [0, 1]:
            if i >= 0:
                keypoints = seq[i][mouse]
                x, y = keypoints[0]*w/imw, keypoints[1]*h/imh

                # Head
                ctx.move_to(x[3], y[3])
                ctx.line_to(x[1], y[1])
                ctx.line_to(x[0], y[0])
                ctx.line_to(x[2], y[2])
                ctx.line_to(x[3], y[3])
                ctx.close_path()

                ctx.set_source_rgba(0.5+0.5*(T-i)/n, 0.5-0.5*abs(T-i)/n, 0.2+mouse*0.6, 1-abs(T-i)/n)
                ctx.fill_preserve()
                ctx.stroke()

                # Body
                ctx.line_to(x[4], y[4])
                ctx.line_to(x[6], y[6])
                ctx.line_to(x[6], y[5])
                ctx.line_to(x[3], y[3])
                ctx.close_path()
                ctx.set_source_rgba(0.2+mouse*0.6, 0.5+0.5*(T-i)/n, 0.5-0.5*abs(T-i)/n, 1-abs(T-i)/n)
                ctx.fill_preserve()
                ctx.stroke()
    for mouse in [0, 1]:
        keypoints = seq[T][mouse]
        x, y = keypoints[0]*w/imw, keypoints[1]*h/imh
        ctx.move_to(x[3], y[3])
        ctx.line_to(x[1], y[1])
        ctx.line_to(x[0], y[0])
        ctx.line_to(x[2], y[2])
        ctx.line_to(x[3], y[3])
        ctx.close_path()
        ctx.set_source_rgba(1, 0.5, 0.1, 1)
        if mouse == 1:
            ctx.set_source_rgba(1, 0.5, 0.8, 1)

        ctx.fill_preserve()
        ctx.set_source_rgb(0, 0, 0)
        ctx.set_line_width(3)
        ctx.stroke()

        # Body
        ctx.line_to(x[4], y[4])
        ctx.line_to(x[6], y[6])
        ctx.line_to(x[6], y[5])
        ctx.line_to(x[3], y[3])
        ctx.close_path()
        ctx.set_source_rgba(0.5, 1, 0.1, 1)
        if mouse == 1:
            ctx.set_source_rgba(0.5, 1, 0.8, 1)
        ctx.fill_preserve()
        ctx.set_source_rgb(0, 0, 0)
        ctx.set_line_width(3)
        ctx.stroke()

# Cell
import random
def augment_sequence(seq):
    """ Flip / rotate a sequence with some random variations"""
    imw, imh = 1024, 570
    if random.random()>0.5:
        for frame in range(len(seq)):
            for m in [0, 1]:
                seq[frame][m][0] = imw-seq[frame][m][0] # X flip
    if random.random()>0.5:
        for frame in range(len(seq)):
            for m in [0, 1]:
                seq[frame][m][1] = imh-seq[frame][m][1] # X flip

    if random.random()>0.7:
        angle = (np.random.rand()-0.5) * (np.pi * 2)
        c, s = np.cos(angle), np.sin(angle)
        rot = np.array([[c, -s], [s, c]])
        for frame in range(len(seq)):
            for m in [0, 1]:
                seq[frame][m] -= np.array([[imw/2]*7, [imh/2]*7])
                seq[frame][m] = np.dot(np.array(seq[frame][m]).T, rot).T
                seq[frame][m] += np.array([[imw/2]*7, [imh/2]*7])


    return seq