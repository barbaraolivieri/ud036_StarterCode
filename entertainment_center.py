import media
import fresh_tomatoes

# Instancias da classe de filmes, com os respectivos atributos
rei_do_show = media.Movie("Rei Do Show", "Historia de P. T. Barnum, criador do modelo de circo atual",
						 "https://imgs.dm.com.br/resized/500/2017/12/5-24.jpg",
						 "https://www.youtube.com/watch?v=r5R6CVp_JzU")
les_mis = media.Movie("Os Miseraveis", "Jean Valjan, um ex-prisioneiro que busca redencao do seu passado",
						 "http://br.web.img3.acsta.net/medias/nmedia/18/90/97/43/20369586.jpg",
						 "https://www.youtube.com/watch?v=IuEFm84s4oI")
grease = media.Movie("Grease", "Danny Zuko e Sandy se conhecem nas ferias e vao estudar na mesma escola",
						 "https://i.ytimg.com/vi/5nlKJKhInxE/movieposter.jpg",
						 "https://www.youtube.com/watch?v=f2CCEixOVVU")

# Definindo os objetos em uma lista 
filmes = [rei_do_show, les_mis, grease]

fresh_tomatoes.open_movies_page(filmes)