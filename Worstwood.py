import fresh_tomatoes
import media_filepy
robo = media_filepy.Worstwood_movies("Robo 2.0",
                                       "Over use of Technology might distroy the current Nature",
                                       "https://upload.wikimedia.org/wikipedia/en/c/cf/2.0_film_poster.jpg",
                                       "https://youtu.be/2wvq8hdGdAw")
bahubali = media_filepy.Worstwood_movies("Bahubali 2",
                                         "Distruction Of Brotherhood",
                                         "https://upload.wikimedia.org/wikipedia/en/thumb/f/f9/Baahubali_the_Conclusion.jpg/220px-Baahubali_the_Conclusion.jpg",
                                         "https://youtu.be/qD-6d8Wo3do")
kuch_kuch_hota_hai = media_filepy.Worstwood_movies("Kuch Kuch Hota Hai",
                                                 "Triangle Love Story",
                                                 "https://i.pinimg.com/originals/14/90/a1/1490a1822f4ee12b903f86adc7055e32.png",
                                                 "https://youtu.be/05i3eIuJLaU")
kabi_khushi_kabi_gum = media_filepy.Worstwood_movies("Kabi Khushi Kabi Gum",
                                                   "Best Family Relationship Movie",
                                                   "https://upload.wikimedia.org/wikipedia/en/thumb/0/0d/KabhiKhushiKabhiGham_Poster.jpg/220px-KabhiKhushiKabhiGham_Poster.jpg",
                                                   "https://youtu.be/7uY1JbWZKPA")
geetha_govindam = media_filepy.Worstwood_movies("Geetha Govindam",
                                              "Convincing a Girl",
                                              "https://images-na.ssl-images-amazon.com/images/I/51XkOYAaT4L._SS500.jpg",
                                              "https://youtu.be/U3dqoAHqagk")
padmavathi= media_filepy.Worstwood_movies("Padmavathi","Great Women Life Story","https://upload.wikimedia.org/wikipedia/en/thumb/7/73/Padmaavat_poster.jpg/220px-Padmaavat_poster.jpg","https://youtu.be/X_5_BLt76c0")
movies=[robo,bahubali,kuch_kuch_hota_hai,kabi_khushi_kabi_gum,geetha_govindam,padmavathi]
fresh_tomatoes.open_movies_page(movies)

