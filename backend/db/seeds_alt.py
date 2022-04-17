from models import User, Post, Follow
from get_db_engine import get_db_engine
from table_utils import create_tables, delete_tables
from sqlalchemy.orm import Session

if __name__ == '__main__':
    engine = get_db_engine()
    delete_tables(engine)
    create_tables(engine)
    session = Session(engine)

    Kevin = User({'username': "Kevin", 'email': "kevinyunas@icloud.com",
                  'password': "password"})
    Daniel = User({'username': "Daniel",
                  'email': "daniel@email.com", 'password': "danielPassword"})
    Gabby = User({'username': "Gabby", 'email': "gabby@email.com",
                 'password': "gabbyPassword"})
    users = [Kevin, Daniel, Gabby]
    session.add_all(users)
    session.commit()
    session.flush()

    beachPost = Post(Kevin.id, "Summer Breeze", "beach.jpg")
    canyonPost = Post(Gabby.id, "Canyon", "canyon.jpg")
    muricaPost = Post(Kevin.id, "Peekaboo", "murica.jpg")
    tracksPost = Post(Kevin.id, "Where to", "tracks.jpg")
    surfsupPost = Post(Gabby.id, "Surfs up", "surfsup.jpg")
    monkPost = Post(Kevin.id, "In another life", "monk.jpg")
    nosotrosPost = Post(Daniel.id, "Nosotros", "nosotros.jpg")
    hashtagPost = Post(Gabby.id, "Hashtag", "hashtag.jpg")
    grafittiPost = Post(Gabby.id, "Fine print", "grafitti.jpg")
    ningunoPost = Post(Gabby.id, "Ninguno", "ninguno.jpg")
    trippyPost = Post(Kevin.id, "Cherry-Coloured Funk", "trippy.jpg")
    trishaPost = Post(Daniel.id, "Trisha", "trisha.jpg")
    liesPost = Post(Gabby.id, "Makes you wonder", "lies.jpg")
    stairsPost = Post(Daniel.id, "Where do they lead", "stairs.jpg")
    daniel10Post = Post(Daniel.id, "Louisiana", "daniel10.jpg")
    mardigrasPost = Post(Daniel.id, "Mardigras awaits", "mardigras.jpg")
    soakPost = Post(Daniel.id, "Soakin in the sun", "soak.jpg")
    hangloosePost = Post(Gabby.id, "Hangloose", "hangloose.jpg")
    sunsetPost = Post(Daniel.id, "Almost golden hour", "sunset.jpg")
    daniel5Post = Post(Daniel.id, "Stay awhile", "daniel5.jpg")

    posts = [beachPost, canyonPost, muricaPost, tracksPost,
             surfsupPost, monkPost, nosotrosPost, hashtagPost,
             grafittiPost, ningunoPost, trippyPost, trishaPost,
             liesPost, stairsPost, daniel10Post, mardigrasPost,
             soakPost, hangloosePost, sunsetPost, daniel5Post]
    session.add_all(posts)

    kevin_gabby_follow = Follow(Kevin.id, Gabby.id)
    kevin_daniel_follow = Follow(Kevin.id, Daniel.id)
    gabby_kevin_follow = Follow(Gabby.id, Kevin.id)
    gabby_daniel_follow = Follow(Gabby.id, Daniel.id)
    daniel_kevin_follow = Follow(Daniel.id, Kevin.id)
    daniel_gabby_follow = Follow(Daniel.id, Gabby.id)

    follows = [kevin_daniel_follow, kevin_gabby_follow,
               gabby_daniel_follow, gabby_kevin_follow,
               daniel_gabby_follow, daniel_kevin_follow]
    session.add_all(follows)

    session.commit()

    session.close()
