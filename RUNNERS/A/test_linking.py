from linking import ObjectState, instantaneous_links, persistence_links


def s(frame,label,x,y,area=100):
    return ObjectState(frame=frame,label=label,x=x,y=y,area=area,mean_intensity=1.0)


def test_instantaneous_identity():
    prev=[s(0,1,0,0),s(0,2,10,0)]
    cur=[s(1,11,1,0),s(1,22,11,0)]
    links=instantaneous_links(prev,cur)
    assert {(a,b) for a,b,_ in links}=={(1,11),(2,22)}


def test_persistence_uses_velocity():
    h=[s(0,1,0,0),s(0,2,10,0)]
    prev=[s(1,11,3,0),s(1,22,7,0)]
    cur=[s(2,111,6,0),s(2,222,4,0)]
    prior={1:11,2:22}
    links=persistence_links(h,prev,cur,prior)
    assert {(a,b) for a,b,_ in links}=={(11,111),(22,222)}


if __name__=="__main__":
    test_instantaneous_identity(); test_persistence_uses_velocity(); print("OK")
