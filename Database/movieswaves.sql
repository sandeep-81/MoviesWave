-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Nov 12, 2024 at 02:23 PM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.0.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `movieswaves`
--

-- --------------------------------------------------------

--
-- Table structure for table `admin`
--

CREATE TABLE `admin` (
  `id` int(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `phone` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `admin`
--

INSERT INTO `admin` (`id`, `name`, `email`, `phone`, `password`) VALUES
(1, 'Amandeep Kaur', 'aman31@gmail.com', '7719427838', '@_Amandeep31'),
(2, 'admin', 'admin@gmail.com', '9876543110', 'admin');

-- --------------------------------------------------------

--
-- Table structure for table `booking`
--

CREATE TABLE `booking` (
  `booking_id` int(255) NOT NULL,
  `movie_name` varchar(255) NOT NULL,
  `movie_date` varchar(255) NOT NULL,
  `show_time` varchar(255) NOT NULL,
  `cinema_name` varchar(255) NOT NULL,
  `ticket_price` int(255) NOT NULL,
  `total_tickets` int(255) NOT NULL,
  `total_amount` int(255) NOT NULL,
  `user_name` varchar(255) NOT NULL,
  `user_mail` varchar(255) NOT NULL,
  `today` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `booking`
--

INSERT INTO `booking` (`booking_id`, `movie_name`, `movie_date`, `show_time`, `cinema_name`, `ticket_price`, `total_tickets`, `total_amount`, `user_name`, `user_mail`, `today`) VALUES
(1247, 'Emergency', '26 OCT 2024', '1:46', 'PVR Friends', 282, 1, 282, 'Amandeep kaur', ' aman@gmail.com', '2024-10-26'),
(2706, 'Kakuda', '8 OCT 2024', '2:10', ' Cinépolis Alpha One,Jalandhar', 220, 2, 440, 'Amandeep kaur', ' amandeep02@gmail.com', '2024-10-24'),
(3996, 'Kakuda', '27 OCT 2024', '1:20', 'PVR Friends', 240, 1, 240, 'Amandeep kaur', ' aman@gmail.com', '2024-10-27'),
(4312, 'Gandhi 3', '7 OCT 2024', '1:34', 'Movie Time cinemas , Amritsar.', 268, 4, 1072, 'sandeep singh', ' s@gmail.com', '2024-10-26'),
(4782, 'Kakuda', '26 OCT 2024', '2:10', ' PVR : INOX Reliance Mall Jalandhar', 220, 1, 220, 'Amandeep kaur', ' aman@gmail.com', '2024-10-26'),
(5920, 'Gandhi 3', '1 NOV 2024', '4:31', ' PVR : INOX Reliance Mall Jalandhar', 262, 2, 524, 'Amandeep kaur', ' aman@gmail.com', '2024-10-26');

-- --------------------------------------------------------

--
-- Table structure for table `cast`
--

CREATE TABLE `cast` (
  `id` int(255) NOT NULL,
  `movie_name` varchar(255) NOT NULL,
  `cast_name` varchar(255) NOT NULL,
  `charcter` varchar(255) NOT NULL,
  `about` varchar(255) NOT NULL DEFAULT 'NA',
  `image` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `cast`
--

INSERT INTO `cast` (`id`, `movie_name`, `cast_name`, `charcter`, `about`, `image`) VALUES
(12, 'Bibi Rajni', 'Yograj Singh', 'Actor', 'Former Indian cricketer, Yograj Singh is also an Indian actor and director. Yograj made his acting debut with the Punjabi film Batwara (1983). Later, he turned director with Vichhora (1994). Yograj has acted in over 33 films including commercially success', 'Movies_Poster/Yograj_Singh.png'),
(13, 'Ardaas Sarbat de bhale di', 'Gippy Grewal', 'Actor,Singer,Producer ', 'Grewal was born Rupinder Singh Grewal; however, he adopted the stage name \"Gippy\" because it was his childhood nickname. He completed his early education at Nankana Sahib Public School in Kot Gangu Rai, Ludhiana. He went on to earn a degree in Hotel Manag', 'Movies_Poster/1698307721.jpeg'),
(14, 'Ardaas Sarbat de bhale di', 'Jasmin Bhasin', 'Actress ', 'Jasmin Bhasin, a versatile Indian actress and model, has carved a niche for herself in the realm of Hindi television and Punjabi cinema. Born into a well-educated and progressive Sikh family, Jasmin\'s journey has been marked by determination, talent, and ', 'Movies_Poster/jasmin-bhasin.jpeg'),
(15, 'Ardaas Sarbat de bhale di', 'Milkit Rauni', 'Actor', 'Primarily known for portraying supporting roles in Punjabi films, Malkeet Rauni has appeared in around forty movies in the course of a career spanning close to a decade. Some of his best known film credits include the Bollywood comedy No Problem (2010), W', 'Movies_Poster/malkit rauni.jpeg'),
(16, 'Ardaas Sarbat de bhale di', 'Nirmal Rishi', 'Actor', 'Nirmal Rishi is a popular Actor. Latest movies in which Nirmal Rishi has acted are Pind Aala School, Allahr Vres, Jatti 15 Murrabean Wali, Majnoo and Vadda Ghar. Nirmal Rishi was born on Nov 01, 1943\n\n', 'Movies_Poster/Nirmal Rishi.jpeg'),
(17, 'Ardaas Sarbat de bhale di', 'Gurpreet Ghuggi', 'Actor', 'Gurpreet Ghuggi was born on 19 July 1971 in Gurdaspur, Punjab, India. He is an actor and writer, known for Dunki (2023), Ardaas Karaan (2019) and Race (2008). He is married to Kuljeet Kaur. They have two children\n', 'Movies_Poster/gurpreet guggi.jpeg'),
(18, 'Ardaas Sarbat de bhale di', 'Prince Kanwaljit Singh\n', 'Writer • Actor • Director ', 'Prince Kanwaljit Singh is an Indian actor and writer who predominantly works in the Punjabi film industry. Having started his career as an actor, he made his debut on the silver screen with Sukhmani in 2010. Following his debut, he mostly played small and', 'Movies_Poster/Prince-Kanwaljit-Singh-Filmography.jpeg'),
(19, 'Sucha Soorma', 'Babbu Mann', 'songwriter,actor,producer.', 'Babbu Maan (born Tejinder Singh Maan on March 29) is a Punjabi singer-songwriter, actor, and producer. Born in the village of Khant Maanpur in the Fatehgarh Sahib District of Punjab, India Babbu Maan has been very fond of playing music since his childhood', 'Movies_Poster/Babbu Mann.jpeg'),
(20, 'Sucha Soorma', 'Sarabjit Cheema', 'Actor,Writer,Singer', 'Sarbjit Singh Cheema is an Indian-Canadian singer and actor who associated with Punjabi language music and films. He made his singing debut with the album Yaar Nachde and He started his film career with Pind Di Kurhi\n', 'Movies_Poster/sarbjit cheema.jpeg'),
(21, 'Sucha Soorma', 'Samiksha Oswal\n', 'Actress,\nProducer', 'Sameksha, is an Indian film and television actress. She has played a range of characters in various series and films, in multiple languages including Tamil, Telugu, Punjabi, Hindi and Kannada. She has directed multiple music videos and films\n', 'Movies_Poster/samekhha oswal.jpeg'),
(22, 'Sucha Soorma', 'Jag Singh', 'Actor,Director,Stunts', 'Jag is known for the Punjabi Movies, Rocky Mental, Medal, Sucha Soorma etc. And the character Gus in Call of Duty Modern Warfare Video game.\n\nJag won the \"Best Antagonist\" at PTC Punjabi\'s Film Awards 2018 for his performance in Rocky Mental.\n\nBeyond acti', 'Movies_Poster/jag singh.jpeg'),
(23, 'Sucha Soorma', 'Suvinder Vicky', 'Actor', 'Suvinder Vicky, a talented actor from Sirsa, Haryana has been making waves in the entertainment industry with his compelling performances. Vicky has made a significant impact in both Bollywood and Punjabi cinema. Recently, the actor is stealing attention ', 'Movies_Poster/-suvinder-vicky.jpeg'),
(24, 'Binny And Family', 'Pankaj Kapur', 'Actor,\nDirector,\nWriter ', 'Pankaj Kapur, born in Ludhiana, Punjab, India, is a highly respected Indian actor, director, and playwright known for his exceptional contributions to the world of Indian cinema, television, and theater. With a career spanning over four decades, Pankaj Ka', 'Movies_Poster/Pankaj_Kapur.jpeg'),
(25, 'Binny And Family', 'Rajesh Kumar', 'Actor', 'Rajesh Kumar was born on January 20, 1975 in Patna, Bihar, India. He is an actor, known for Yeh Meri Family (2018), Sarabhai V/S Sarabhai (2004) and Neeli Chatri Waale (2014).\n', 'Movies_Poster/Rajesh-Kumar.jpg'),
(26, 'Binny And Family', 'Anjini Dhawan', 'Actress', 'Anjini is the granddaughter of Anil Dhawan, the brother of David Dhawan. She will make her debut with Binny and Family, which also stars Pankaj Kapur, Himani Shivpuri, Rajesh Kumar, and Charu Shankar. It is slated to release on September 20, 2024.\n', 'Movies_Poster/xyz.jpg'),
(27, 'Binny And Family', 'Himani Shivpuri', '\nActress', 'Himani Shivpuri was born on October 24, 1960 in Dehra Dun, Uttar Pradesh, India. She is an actress, known for Happu Ki Ultan Paltan (2019), Kabhi Khushi Kabhie Gham... (2001) and Dilwale Dulhania Le Jayenge (1995). She was previously married to Gyan Shivp', 'Movies_Poster/abc.jpeg'),
(28, 'Kahan Shuru Khatam', '\n\nDhvani Bhanushali', 'Music Artist,Actress', 'Dhvani Bhanushali was born on 2 June 1998 in Mumbai, Maharashtra, India. She is a music artist and actress, known for Satyameva Jayate (2018), Dhvani Bhanushali & Nikhil D\'Souza: Vaaste (2019) and Saaho (2019).\n', 'Movies_Poster/Singerr_3 (1).jpg'),
(29, 'Kahan Shuru Khatam', 'Dhvani Bhanushali\n', 'Actor', 'Aashim Gulati was born on September 15, 1990 in Delhi, India. He is an actor, known for Taj: Divided by Blood (2023), Hostages (2019) and Dil Sambhal Jaa Zara (2017).\n', 'Movies_Poster/AashimGulati3.jpg'),
(30, 'Kahan Shuru Khatam', 'Rajesh Sharma', 'Actor', 'Rajesh Sharma was born on October 8, 1980 in Ludhiana, Punjab, India. He is an actor, known for The Dirty Picture (2011), Toilet: A Love Story (2017) and Bajrangi Bhaijaan (2015). He has been married to Sangeeta Sharma since 2011. He was previously marrie', 'Movies_Poster/python project/images.jfif'),
(31, 'Kahan Shuru Khatam', 'Supriya Pilgaonkar\n', 'Actor, Director,Producer\n', 'Supriya Pilgaonkar is a distinguished Indian television and film actress, renowned for her prolific work in Hindi and Marathi language television shows. Born as Supriya Sabnis in Mumbai, Maharashtra, she hails from a Maharashtrian family. Her journey in t', 'Movies_Poster/Supriya-Pilgaonkar-2.jpg'),
(32, 'Kahan Shuru Khatam', 'Akhilendra Mishra', 'Actor', 'Akhilendra Mishra is an Indian film and television character actor best known for his role as Kroor Singh in the 1990s Doordarshan fantasy television series Chandrakanta. His other notable works include the character of Mirchi Seth in the 1999 critically ', 'Movies_Poster/efg.jpg'),
(33, 'Adbhut', 'Nawazuddin Siddiqui\n', 'Actor,Producer, Director ', 'Nawazuddin Siddiqui (born 1974) is an Indian film actor who has appeared in some of Bollywood\'s major films including, Black Friday (2004), New York (2009), Peepli Live (2010), Kahani (2012), Gangs of Wasseypur (2012) and Gangs of Wasseypur - Part 2 (2012', 'Movies_Poster/images.webp'),
(34, 'Adbhut', 'Diana Penty\n', 'Actress', 'Diana Penty was born in Bombay on November 2nd, 1985 to a Christian mother and a Parsi father. She attended St. Agnes high school in Bombay, and graduated with a Bachelors degree in Mass Communication from the St. Xavier\'s University in Bombay.\n\n', 'Movies_Poster/diana-penty-.webp'),
(35, 'Adbhut', 'Shashank Shende', 'Actor \nProducer \nWriter', 'Shashank Shende is an Indian actor who has starred in several Hindi and Marathi films. His most popular roles were seen in the movies Kaminey, Ishqiya, Chittagong, Aaghaat and Force. One of his other prominent roles was that of Stanley\'s Chacha in the 201', 'Movies_Poster/ShashankShende.jpg'),
(36, 'Adbhut', 'Shreya Dhanwanthary\n', 'Actress,\nDirector,\nWriter', 'Shreya Dhanwantary, is an Indian actress, model and author who works predominantly in the Hindi and Tamil film industries. After her birth, Dhanwanthary\'s family moved to Dubai, where she spent most of her childhood. She was raised in both the Middle East', 'Movies_Poster/88870292.jpg'),
(37, 'Adbhut', 'Rohan Mehra', 'Actor\n', 'Rohan Mehra is an Indian actor who works in films, web shows and Indian television He is known for his roles in Indian TV shows like Yeh Rishta Kya Kehlata Hai as Naksh Singhania, Sasural Simar Ka as Sameer Kapoor, he was also a finalist on the reality TV', 'Movies_Poster/Rohan Mehra.jpg'),
(38, 'Emergency', 'Kangana Ranaut\n', 'Actress,Director,\nProducer', 'Kangana was born on 23 March 1987 in Bhambla, near Manali, which is in the Mandi district of Himachal Pradesh. Her dad Amardeep is a businessman and her mom Asha is a schoolteacher. She has two sisters and a younger brother. Her grandfather was an IAS Off', 'Movies_Poster/kangana-ranaut-wedding.jpg'),
(39, 'Emergency', 'Manisha Koirala', 'Actress,\nProducer,\nSoundtrack', 'Manisha Koirala (born 16 August 1970) is a Nepali actress who mainly appears in Bollywood, though she has worked in several South Indian and her native country\'s films. Noted for her acting prowess, Koirala is the recipient of several accolades, including', 'Movies_Poster/16manisha1.jpg'),
(40, 'Emergency', 'Anupam Kher\n', 'Actor,\nProducer,\nMusic Department', 'Anupam Kher is a renowned Indian actor who has worked extensively in the Indian film industry, as well as in international films and television shows. He is known for his versatile acting skills and has portrayed a wide range of characters throughout his ', 'Movies_Poster/anupam_kher_film_success-three_four.jpg'),
(41, 'Emergency', 'Mahima Chaudhry', 'Actress', 'First got noticed as a model for Pepsi, where she was over-shadowed by Aishwarya Rai Bachchan. Career launched by Subhash Ghai, who also launched Madhuri Dixit, \'Meenakshi Seshadri\' and Manisha Koirala. Changed her screen name to Mahima as Subhash Ghai wa', 'Movies_Poster/anupam_kher_film_success-three_four.jpg'),
(42, 'Emergency', 'Satish Kaushik', 'Actor,\nDirecor,\nProducer', 'Satish Chandra Kaushik was a well-known Indian actor and comedian. He was also a director, producer, and screenwriter. Kaushik graduated from Kirori Mal College, Delhi, and received professional training from the National School of Drama, Delhi, and the F', 'Movies_Poster/c9b21409d434f7078626bd7961099f4c1678367110883380_original.jpg'),
(43, 'Emergency', 'Vishak Nair\n', 'Actor', 'Vishak Nair is an Indian actor known for his roles in numerous feature films in Malayalam and Hindi.He made his debut in the 2016 coming-of-age drama \"Aanandam\", which received critical acclaim and made him a household name in Kerala.\n\nFollowing his debut', 'Movies_Poster/vishak-nair-1724949081.jpg'),
(44, 'Emergency', 'Shreyas Talpade\n', 'Actor,\nProducer,\nDirector', 'Shreyas Talpade, born in Mumbai, Maharashtra, India, is a versatile Indian actor known for his work in Bollywood and Marathi cinema. He has showcased his acting prowess across various genres, earning recognition for his comic timing, versatility, and impa', 'Movies_Poster/shreyas-talpade-2154-20-09-2017-01-26-36.jpg'),
(45, 'Shukrana', 'Amrit Maan', 'Actor,singer,songwriter', 'Amrit Maan is a prominent figure in the Punjabi entertainment industry, known for his multifaceted talents as a singer, lyricist, and actor. He gained popularity with his distinctive voice and powerful lyrics, often blending traditional Punjabi themes wit', 'Movies_Poster/python project/amrit mann.jfif'),
(46, 'Shukrana', '	Arshvir Kaur Bajwa', '	Actor • Director • Producer', 'Neeru Bajwa is a Canadian born Indian actress. She works in the Punjabi film industry. Neeru Bajwa is a Punjabi actress who is known for her television appearances in Astitva...Ek Prem Kahani (2003), Jeet (2003) and Nach Baliye 2 (2006). Her popular movie', 'Movies_Poster/python project/neru bajwa.webp'),
(47, 'Shukrana', 'Jaswant Singh', 'Actor', 'Jass Bajwa is an Indian singer, lyricist and actor, who is known for his work in the Punjabi music and film industry. He made his debut as a singer with his 2014 album Chakvi Mandeer. The album was a hit with the audience and Jass was suddenly in the big ', 'Movies_Poster/jass bajwa.jpg'),
(48, 'Shukrana', 'Harby Sangha\n', 'Actor', 'Harby Sangha, also known as Harbilas Sangha, is an actor who appears primarily in supporting roles in Punjabi cinema. Some of his most popular roles have come in movies like Bambukat (2016), Nikka Zaildar (2016) and its sequel Nikka Zaildar 2 (2017). Othe', 'Movies_Poster/python project/download.webp'),
(49, 'Shukrana', 'Gurpreet Kaur Bhangu\n', 'Actor', 'Gurpreet Bhangu is a renowned Punjabi actress who started her career with theatre, and was quite involved in the sphere ever since she was a college student. After getting married in 1983, she took a brief hiatus from theatre and rejoined in 1996. Her not', 'Movies_Poster/gurpreet-bhangu-1072183-1709030451.jpg'),
(50, 'Shukrana', 'Seema Kaushal\n', 'Actor', 'Seema Kaushal is an Indian actress who appears mainly in supporting roles in Punjabi films and Bollywood. She is best known for her role in the Bollywood comedy Luv Shuv Tey Chicken Khurana (2012) and in Punjabi films like Munde U.K. De: British by Right ', 'Movies_Poster/seema.jpg'),
(51, 'Shukrana', 'Gurmeet saajan', 'Actor', 'Gurmeet Saajan is a respected figure in the Punjabi entertainment industry, particularly known for his work as an actor in Punjabi cinema and theater. With a career spanning several decades, he has built a reputation for portraying a wide range of roles, ', 'Movies_Poster/python project/gummet sajan.webp'),
(52, 'Shahkot', '	Gursharanjot Randhawa', '	Music • Singer • Lyricist • Producer • Actor', 'The High Rated Gabru hitmaker, Guru Randhawa is a Punjabi singer and songwriter who made his debut in 2013 with the album titled Page One, which comprised songs like `Billo On Fire`, `My Jugni`, `Khali Bottlan`, and `Modern Thumka` among many others. It w', 'Movies_Poster/Randwawa.webp'),
(53, 'Shahkot', 'Isha Talwar', 'Actor', 'Isha Talwar rose to fame with an award-winning performance in her lead role debut in the Malayalam film Thattathin Marayathu (2012). Apart from predominant work in the Malayalam film industry, the actress has featured in a handful of movies in Hindi, Tami', 'Movies_Poster/Isha_Talwar.jpg'),
(54, 'Shahkot', 'Raj Babbar', 'Actor', 'Raj Babbar is a Hindi and Punjabi film actor and politician. After graduating from the National School of Drama, he moved to Mumbai to start his film career. Raj Babbar made his debut in the film Kissa Kursi Ka (1977) and later went on to star in the hit ', 'Movies_Poster/Raj Babbar.jfif');

-- --------------------------------------------------------

--
-- Table structure for table `cinemas`
--

CREATE TABLE `cinemas` (
  `id` int(255) NOT NULL,
  `cinema_name` varchar(255) NOT NULL,
  `address` varchar(255) NOT NULL,
  `road` varchar(255) NOT NULL,
  `district` varchar(255) NOT NULL,
  `pincode` varchar(255) NOT NULL,
  `screeens` int(255) NOT NULL,
  `seats` int(255) NOT NULL,
  `phone` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `opening_time` varchar(255) NOT NULL,
  `closing_time` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `cinemas`
--

INSERT INTO `cinemas` (`id`, `cinema_name`, `address`, `road`, `district`, `pincode`, `screeens`, `seats`, `phone`, `email`, `opening_time`, `closing_time`) VALUES
(1, 'PVR Friends', 'PVR LTD OLD', 'Post Office Road', 'Jalandhar', '144001', 7, 240, '9874554987', 'pvr@gmail.com', '09:00 AM', '10:00 PM'),
(2, 'PVR : Inox Curo, Jalandhar', 'Curo High Street, 66 Feet Road, Punjabi Bagh Extension, IsharPuri Colony, Mithapur, Near Dulhan Palace, Jalandhar.', 'Curo High Street, 66 Feet Road', 'Jalandhar', ' 144022', 4, 250, '+91-124-4708100', 'info@pvrcinemas.com', ' 8:00 AM ', '9:00 PM'),
(3, ' PVR : INOX Reliance Mall Jalandhar', 'Puda Jalandhar, opp. Govt. Medical College, Part-II, Choti Baradari, Jalandhar.', 'Choti Baradari, Jalandhar', 'Jalandhar', '144001', 5, 250, ' 080802 11111', 'info@pvrcinemas.com', '12:00 PM', '11:59 PM'),
(4, 'PVR : Cinemas MBD Neopolis Mall', 'MBD Neopolis Mall, BMC Chowk, Sehdev Market, Jalandhar.', 'Jandiala Road, Sehdev Market, Next To Radisson Hotel, Jalandhar.', 'Jalandhar', '144001', 5, 250, '+91 8800900009', 'info@pvrcinemas.com', '9:00 AM ', '11:00 PM'),
(5, 'PVR : GRD CINEMAS Jalandhar.', ' BIG BAZAAR VIVA COLLAGE MALL, OLD, Grand Trunk Rd, Pragpur Village, Paragpur, Jalandhar.', ' Pragpur Village, Paragpur, Jalandhar.', 'Jalandhar', '144005', 3, 150, '+91-935747732', 'info@pvrcinemas.com', '10:00 AM', '11:00 PM'),
(6, 'Movie Time cinemas , Amritsar.', 'Omaxe Novelty Mall, 10, Ranjit Avenue, Amritsar, Punjab, India', ' Ranjit Avenue', 'Amritsar', '143001', 4, 600, '+91 98765 43210 ', 'info@movietime.com', '10:00 AM', '11:00 PM'),
(7, ' Cinépolis Alpha One,Jalandhar', 'Address: Alpha One Mall, 3rd Floor, GT Road, Amritsar, Punjab, India\n', 'GT Road', 'Amritsar', '143001', 6, 1, '+91 183 258 1800', ' info@cinepolis.com', '10:00 AM', '11:00 PM'),
(8, ' INOX, Amritsar', ' Trilium Mall, Circular Road, Amritsar, Punjab, India', ' Circular Road', 'Amritsar', '143001', 5, 1, '+91 183 500 4346 ', 'contact@inoxmovies.com', '10:00 AM', '11:00 PM'),
(9, 'PVR Suraj Chanda Tara Cinema,Amritsar', 'Queens Road, Amritsar, Punjab, India', 'Queens Road', 'Amritsar', '143001', 3, 600, '+91 183 506 5656 ', ' contact@pvrcinemas.com', '9:30 AM', '11:00 PM'),
(10, ' Cinépolis Nexus, Amritsar', 'Nexus Amritsar Mall, GT Road, Amritsar, Punjab, India', 'GT Road', 'Amritsar', ' 143001', 6, 1, '+91 183 258 1800 ', 'info@cinepolis.com ', '10:00 AM', '11:00 PM'),
(11, 'Sangam Cinema ,Amritsar.', 'Maqbool Road, Amritsar, Punjab, India', 'Maqbool Road.', 'Amritsar', '143001', 1, 400, '+91 183 222 5555', 'info@sangam.com', '10:00 AM', '11:00 PM'),
(12, 'Panther Cinema Theatre , Amritsar', 'Majitha Road, Amritsar, Punjab, India', 'Majitha Road.', 'Amritsar', '143001', 1, 400, '+91 183 255 1234', 'info@panther cinema.com', '10:00 AM', '11:00 PM'),
(13, 'Inder Palace Cinema , Amritsar.', ' Lawrence Road, Amritsar, Punjab, India', ' Lawrence Road.', 'Amritsar', '143001', 1, 500, '+91 183 222 7890', 'info@inder.com', '10:00 AM', '11:00 PM'),
(14, 'Sher-e-Punjab 7D Movie Theater ,Amritsar.', 'Golden Temple Road, Inside Jallianwala Bagh, Amritsar, Punjab, India.', 'Golden Temple Road.', 'Amritsar', '143006', 1, 150, '+91 98765 43210', 'info@Sher-e-Punjab.com', '9:00 AM', '8:00 PM'),
(15, ' VR Ambarsar', ' VR Ambarsar Mall, GT Road, Amritsar, Punjab, India.\n', 'GT Road', 'Amritsar', '143001', 7, 1, '+91 183 258 4567', ' info@vrambarsar.com ', '10:00 AM', '11:00 PM'),
(16, 'Chitra Talkies , Amritsar.', ' Katra Jaimal Singh, Amritsar, Punjab, India', 'Katra Jaimal Singh.', 'Amritsar', ' 143001', 1, 500, '+91 183 255 6789 ', 'info@Chitratalkies.com', '10:00 AM', '11:00 PM'),
(17, ' Adarsh Cinema , Amritsar.', 'Majitha Road, Amritsar, Punjab, India', 'Majitha Road.', 'Amritsar', ' 143001', 1, 400, '+91 183 254 3210 ', 'info@Adarshcinema.com', '10:00 AM ', '11:00 PM'),
(18, ' Amrit Talkies , Amritsar.', 'Katra Jaimal Singh, Amritsar, Punjab, India.', 'Katra Jaimal Singh.', 'Amritsar', '143001', 1, 300, ' +91 183 255 4321 ', 'info@Amrittalkies.com', '10:00 AM ', '11:00 PM'),
(19, ' GE Cinemas, Barnala.', 'Near Sherpur Chowk, Bathinda Road, Barnala, Punjab', 'Bathinda Road', 'Barnala', '148101', 2, 500, '+91 8800900009', 'info@GEcinemas.com', '9:30 AM', '11:00 PM'),
(20, 'PVR INOX Silver Arc Mall , Ludhiana.', ': Silver Arc Mall, 622 Ferozpur Road, Gurdev Nagar, Ludhiana, Punjab , India', 'Silver Arc Mall, 622 Ferozpur Road', 'Ludhiana', '141001', 5, 250, ' +91 8800900009', 'info@Inoxsilver.com', '12:00 AM', '12:00 PM'),
(21, ' Cinépolis MBD Neopolis , Ludhiana.', ' MBD Neopolis Mall, Ferozepur Road, Ludhiana, Punjab', 'Ferozepur Road.', 'Ludhiana', ' 141012', 5, 1200, '+91 183 255 4321', 'info@Cinepolis.com', '10:00 AM', '11:00 PM'),
(22, ' PVR INOX, Avon City Mall.', 'Avon City Mall, Ferozepur Road, Ludhiana, Punjab, India', 'Ferozepur Road', 'Ludhiana', '141012', 5, 1, '+91 161 501 2345', ' contact@pvrcinemas.com', '10:00 AM', '11:00 PM'),
(23, ' Wave Cinemas, Ludhiana\n', 'Address: Westend Mall, Ferozepur Road, Ludhiana, Punjab, India\n', 'Ferozepur Road', 'Ludhiana', '141012', 5, 1, '+91 161 468 7800', 'contact@pvrcinemas.com', '10:00 aM ', '11:00 PM'),
(24, 'Shingaar Cinema ,  Ludhiana.', ' Near Clock Tower, Old GT Road, Ludhiana, Punjab, India', ' Old GT Road.', 'Ludhiana', '141008', 1, 400, '+91 161 272 1234', 'info@Shingaar.com', '10:00 AM', '11:00 PM'),
(25, ' Orient Cinema ,  Ludhiana.', ' Field Ganj, Ludhiana, Punjab, India.', ' Field Ganj.', 'Ludhiana', '141008', 1, 300, ' +91 161 244 5678 ', 'Cin@Orient.com', '10:00 AM ', '11:00 PM'),
(26, ' Society Theatre, Ludhiana.', 'Near Chaura Bazar, Old GT Road, Ludhiana, Punjab, India', 'Old GT Road.', 'Ludhiana', ' 141008', 1, 400, '+91 161 273 8900', 'Cin@ Societytheatre.com', '10:00 AM', '11:00 PM'),
(27, ' Preet Palace Cinema, Ludhiana', 'Shimlapuri, Ludhiana, Punjab, India.', 'Shimlapuri.', 'Ludhiana', ' 141003', 1, 350, ' +91 161 251 2345 ', 'Cin@ Preetpalacecinema.com', '10:00 AM ', '11:00 PM'),
(28, ' Nirmal Theatre ,Ludhiana.', ' Near Sabzi Mandi, Chaura Bazar, Ludhiana, Punjab, India\n', 'Chaura Bazar', 'Ludhiana', ' 141008', 1, 400, '+91 161 274 5678', 'Cin@ Nirmal Theatre.com', '10:00 AM', '11:00 PM'),
(29, ' V2V Cinemas , Ludhiana.', ' Sunder Nagar, Ludhiana, Punjab, India', ' Sunder Nagar', 'Ludhiana', '141007', 2, 600, '+91 161 267 8900', 'Cin@ Sunder Nagar.com', '10:00 AM', '11:00 PM'),
(30, ' Q Cinemas, The Peninsula Mall, Bathinda', 'The Peninsula Mall, Goniana Road, Bathinda, Punjab, India', 'Goniana Road', 'Bathinda', 'v', 3, 151001, '+91 161 267 8900 ', 'Cin@ Q Cinemas.com', '10:00 AM', '11:00 PM'),
(31, ' Fun Cinemas, Mittal City Mall', ' Mittal City Mall, Vishal Nagar, Amrik Singh Road, Bathinda, Punjab, India.', ' Amrik Singh Road.', 'Bathinda', ' 151001', 4, 1, '+91 91164 500804', 'info@ Fun Cinemas.com', '10:00 AM', '11:00 PM'),
(32, 'Silver Bird Cinemas', 'National Highway 95, Ferozepur, Punjab.', 'National Highway 95.', 'Ferozepur', '152002', 3, 300, '+91 8725004761', 'Cin@Silver Bird.com', '8:00 AM', '11:55 PM'),
(33, 'Miraj Cinemas', 'Kundan Palace, Hanumangarh Road, Hanumangarh', 'Hanumangarh Road.', 'Ferozepur', '152002', 4, 600, '+91 88797 71585', '+91 88797 71585', '10:00AM', '11:00 PM'),
(34, 'NOVA OHM ORBIT Sanjeev Cinema', ' Army Cantonment Rd, Radha Swami Colony, Gandhi Nagar, Fazilka.', ' Gandhi Nagar.', 'Ferozepur', '152123', 3, 400, '+91 96156 13333', 'Cinema@Novaohmorbit.com', '8:00 AM', '11:00 PM'),
(35, ' Carnival Cinemas (Mr Mall).', ' Mr Mall, Ferozepur City, Punjab.', 'Ferozepur City', 'Ferozepur', '152001', 3, 250, '+91 7400438013', 'Cinmea@ Carnivalcinemas.com', '10:00 AM', '11:00 PM'),
(36, 'Harkishan Multiplex.', 'Near Mall Road, Ferozepur District, Punjab.', 'Near Mall Road', 'Ferozepur', '152001', 3, 250, '+91 70870606601', 'Cin@Harkishanmultiplex.com', '10:00 AM', '10:00 PM'),
(37, ' Gill Multiplex J.D.S Cinemas.', ' Gills Palace, Circular Road, Balbir Basti, Faridkot.', 'Circular Road.', 'Faridkot', '151203', 1, 400, '+91 9056076040', 'info@Gillmultiplex.com', '10:00 AM', '11:00 PM'),
(38, ' Orbit Cinemas.', 'Faridkot Road, Near Railway Crossing, Kot Kapura.', 'Faridkot Road.', 'Faridkot', '151204', 2, 300, '151204', 'orbitmultiplexkkp@gmail.com', '9:00 AM', '11:00 PM'),
(39, ' Fun Plaza Multiplex.', 'Kotkapura - Moga Road, Kot Kapura.', 'Moga Road.', 'Faridkot', '151204', 1, 300, '+91 92572 80007', 'info@Funplaza.com', '9:00 AM', '11:00 PM'),
(40, 'Smart Cinemaz', 'Modern Valley, Fatehgarh Sahib.', 'Fatehgarh Sahib.', 'Fatehgarh Sahib', '140407', 2, 400, '+91 88720 01234', 'info@Smartcinemaz.com', '9:00 AM', '11:00 PM'),
(41, 'Shyam Cineplex', 'Amloh Road, Mandi Gobindgarh, Fatehgarh Sahib, Punjab\n', 'Mandi Gobindgarh.', 'Fatehgarh Sahib', ' 147301 ', 4, 250, '+91 8427621611 ', 'info@Shyamcineplex.com', '9:00 AM', '11:00 PM'),
(42, ' V2V Cinema (Pristine Mall) ', 'Pristine Mall, Fatehgarh Sahib, Punjab', 'Fatehgarh Sahib', 'Fatehgarh Sahib', ' 140407', 3, 500, '+91 9814791026', 'info@ V2Vcinema ', '9:00 AM', '11:00 PM'),
(44, 'Omjee Cinemas Pristine Mall.', ' Pristine Mall, Grand Trunk Road, Khanna, Punjab ', 'Grand Trunk Road.', 'Fatehgarh Sahib', 'Grand Trunk Road.', 3, 300, ' 098147 91026', 'info@Omjeecinemas.com ', '9:00 AM', '11:00 PM'),
(45, 'PVR Celebration Bazar.', 'Ground Floor, The Celebration Bazaar, Dream City Rd, Khanna, Fatehgarh Sahib, Punjab', 'The Celebration Bazaar.', 'Fatehgarh Sahib', '141401', 6, 250, '+91 79733 86609', 'info@pvrcinemas.com', '10:30 AM', '11:00 PM'),
(46, 'Adarsh Theater', 'Near Bassi Road, Adarsh Nagar, Fatehgarh Sahib, Punjab. Near Bassi Road, Adarsh Nagar, Fatehgarh Sahib, Punjab .', 'Fatehgarh Sahib.', 'Fatehgarh Sahib', '140406', 1, 200, '+ 91 8748468383', 'info@ Adarshtheater.com', '10:00 AM', '11:00 PM'),
(47, ' Ritz Multiplex', 'Located on Chandigarh Road, Fatehgarh Sahib, Punjab.', ' Fatehgarh Sahib.', 'Fatehgarh Sahib', '140406', 3, 460, '+ 91 3373787823', 'info@ritzmultiplex.com', '10:00 AM', '11:30 PM'),
(48, 'Solitaire Cinemas.', 'Near Ranjit Singh Park, Gurdaspur,Punjab.', 'Near Ranjit Singh Park', 'Gurdaspur', ' 143521', 4, 900, ' +91 98765 43210 ', 'info@solitairecinemas.com', '10:00 AM', '11:00 PM'),
(49, ' One Cinemas.', 'Near Bus Stand,Gurdaspur,Punjab.', 'Near Bus Stand', 'Gurdaspur', '143521', 3, 600, '+91 98765 43211', ' info@onecinemas.com ', '10:30 AM', '11:30 PM'),
(50, 'Krishna Cinema.', ' Near Civil Hospital,Gurdaspur,Punjab.', ' Near Civil Hospital.', 'Gurdaspur', ' 143521', 2, 300, '+91 98765 43212 ', 'info@krishnacinema.com', '11:00 AM', '11:00 PM'),
(51, 'Onam Cineplex', 'Near Railway Station,Gurdaspur,Punjab.', 'Near Railway Station.', 'Gurdaspur', '143521', 5, 1, '+91 98765 43213 ', 'info@onamcineplex.com', '10:00 AM', '11:00 PM'),
(52, 'Carnival Cinemas', 'Near Bus Stand,Gurdaspur,Punjab.', 'Near Bus Stand,', 'Gurdaspur', ' 143521', 6, 12, '+91 98765 43214 ', 'info@carnivalcinemas.com', '10:00 AM', '11:00 PM'),
(53, ' Miraj Cinemas.', 'Near Main Market,Gurdaspur,Punjab.', 'Near Main Market.', 'Gurdaspur', '143521', 4, 800, '+91 98765 43215', ' info@mirajcinemas.com', '10:00 AM', '11:30 PM'),
(54, 'Miraj Cinemas (JS Eminent Mall).', 'Near Hoshiarpur Road,Hoshiarpur,Punjab.', 'Near Hoshiarpur Road', 'Hoshiarpur', '146001', 5, 1, '+91 98765 43216', 'info@mirajcinemas.com', '10:00 AM', '11:00 PM'),
(55, 'President Cinemas', 'Near Civil Hospital,Hoshiarpur,Punjab.', 'Near Civil Hospital.', 'Hoshiarpur', ' 146001', 3, 600, ' +91 98765 43217', 'info@presidentcinemas.com ', '10:30 AM', '11:00 PM'),
(56, ' Swarn Cineplex.', 'Near Hoshiarpur Road,Hoshiarpur ,Punjab.', 'Near Hoshiarpur Road.', 'Hoshiarpur', '146001', 4, 800, '+91 98765 43218 ', 'info@swarncineplex.com', '10:00 AM', '11:00 PM'),
(57, 'AG Star Cinemas.', 'Near Main Market, Hoshiarpur,Punjab.', 'Near Main Market.', 'Hoshiarpur', ' 146001', 5, 900, '+91 98765 43219', 'info@agstarcinemas.com', '10:30 AM', '11:00 PM'),
(58, ' Time Cinemas.', 'Near Bus Stand, Hoshiarpur ,Punjab.', 'Near Bus Stand.', 'Hoshiarpur', '146001', 4, 800, '+91 98765 43220', 'info@timecinemas.com', '10:00 AM', '11:30 PM'),
(60, 'KBP Shiraz Cinema', 'Near Hoshiarpur Road,Punjab.', 'Near Hoshiarpur Road', 'Hoshiarpur', ' 146001', 3, 500, '+91 98765 43221', 'info@kbpshirazcinema.com ', ' 10:30 AM', '11:00 PM'),
(61, 'Jagatjit cinema.', 'Sultanpur Rd, Shivaji Nagar, Kapurthala, Punjab.', 'Shivaji Nagar.', 'Kapurthala', '144602', 1, 200, '+91 182 223 2313', 'info@Jagatjitcinema.com', '9:00 AM', '11:00 PM'),
(62, 'Sainik school Auditorium', 'Sainik School, Kapurthala, Punjab', 'Sainik School, Kapurthala.', 'Kapurthala', '144602', 1, 250, '+ 915677787934', 'info@Sainik.com', '10:00 AM', '11:00 PM'),
(63, 'Golden Cinemas.', 'Grand Mall, Barnala-Mansa Sisra Road, Near Nehru College, Mansa,Punjab', 'Mansa Sisra Road.', 'Mansa', '151505', 1, 300, '+91 3455888804', 'info@Goldencinemas', '10:00 AM', '12:00 PM'),
(64, 'Skyee Cinema.', 'Bareta Jakhal Road, Near Football Chowk, Budhlada, Mansa, Punjab.', 'Bareta Jakhal Road.', 'Mansa', '151502', 1, 200, '+91 8847690008', 'info@Skyeecinema.com', '10:00 AM', '11:00 PM'),
(65, 'Samrat Cinema', ' Samrat Palace, Khokhar Road, Near Over Bridge, Mansa, Punjab.', 'Khokhar Road.', 'Mansa', '151505', 1, 465, '+91 9876171259', 'info@ Samratcinema', '10:00 AM', '11:00 PM'),
(66, '9D Cinema', 'Ocean Mall, Near Paniwala, Mansa', ' Near Paniwala, Mansa', 'Mansa', '151505', 3, 150, '+91 9357373173', 'info@9Dcinema.com', '10:00 AM', '11:00 PM'),
(67, 'Cineroyale Cinemas - Chokha Empire.', 'Barnala-Amritsar Bypass Road, Kartar Nagar, Bugipura Chowk, Moga, Punjab ', 'Kartar Nagar.', 'Moga', '142001', 4, 250, ' +91 9814137101', 'info@Cineroyalecinemas.com', '10:00 AM', '10:00 AM'),
(68, 'Neelam Nova Cinemas', 'Moga-Ludhiana GT Road, opposite Focal Point, Gtr Moga, Industrial Area, Moga, Punjab.', 'Moga-Ludhiana GT Road.', 'Moga', '142001', 1, 250, '+91 34356727332', 'info@Neelamnova.com', '10:00 AM', '11:00 PM'),
(69, 'Orbit Multiplex', 'Jira Road, Dashmesh Nagar, Near City Park Resorts, Moga, Punjab ', 'Jira Road', 'Moga', '142001', 3, 400, ' +91 7888501537', 'info@Orbitmultiplex.com', '10:00 AM', '11:00 PM'),
(70, 'FunIsland Cinemas', 'Moga Road, near Talwandi Chowk, Talwandi Bhai, Punjab ', 'Moga Road', 'Moga', '142050', 1, 300, ' +91 92572 03257', 'info@FunIslandcinemas.com', '9:00 AM', '11:00 PM'),
(71, 'Lal Palace Cineplex ', 'Moga Road, Kothe Fateh Din De, Jagraon, Punjab. ', 'Moga Road', 'Moga', '142026', 2, 400, '+91 79734 75242', 'info@Lalpalace.com', '11:00 AM', '12:00 PM'),
(72, 'Star Omjee Cinemas', 'Opposite Power House, Sidhwan Bet Road, Jagraon, Punjab.', 'Sidhwan Bet Road.', 'Moga', '142026', 2, 250, '+91 8999373339', 'info@StarOmjee.com', '9:00 AM', '11:00 PM'),
(73, 'Carnival Cinemas MSP', 'National Highway 1A, Jai Jammu Bypass Road, Near Indian Oil Depot, Pathankot, Punjab.', 'Jai Jammu Bypass Road.', 'Pathankot', '145001\n', 2, 330, '+91 186 508 0111', 'info@Carnivalcinemas', '9:30 AM', '11:00 PM'),
(74, 'PVR Cinemas (Novelty Mall)', 'Novelty Mall, Dalhousie Road, Pathankot, Punjab', 'Dalhousie Road', 'Pathankot', '145001', 3, 800, '+91 2390489823', 'info@Cinemas.com', '10:00 AM', '11:00 PM'),
(75, 'Jadooz Cinema', 'Pathaanakot Road, Nurpur - (Jandian Gallery, Jassur, Raja Ka Bagh)', 'Pathaanakot Road', 'Pathankot', '145001 ', 2, 400, ' 0186-2220000', 'info@jadooz.com ', '10:00 AM', '11:00 PM'),
(76, 'Moonlight Cineplex', 'Near New Bus Stand,Pathankot Road,Punjab', 'Pathankot Road', 'Pathankot', '145001', 3, 300, '0186-2220200', 'info@Moonlightcineplex.com', '10:00 AM', '11:00 PM'),
(77, 'Solitaire Kesar Cinemas', 'Near Kesar Hospital, Pathankot', 'Pathankot Road.', 'Pathankot', '145001', 5, 650, '0186-2200200 ', 'info@Solitairekesar.com ', '10:00 AM', '11:00 PM'),
(78, 'PVR Cinemas (VRC City Mall)', ' VRC City Mall, Nabha Road,Patiala', 'Nabha Road.', 'Patiala', '147001', 7, 1, ' 0175-5002444 ', 'info@PVRcinemas.com', '10:00 AM', '11:00 PM'),
(79, 'Prime Cinemas', 'Near P.U. Campus, Sector 25, Patiala,Punjab.', 'Near P.U. Campus.', 'Patiala', '147001', 5, 800, '0175-5011000', 'info@Primecinemas.com', '10:00 AM', '11;00 PM'),
(80, 'Om Jee Cinemas', 'Near Rajindra Hospital, GT Road,Patiala.', 'GT Road.', 'Patiala', '147001 ', 3, 400, ' 0175-5015000 ', 'info@OmJeecinemas.com', '10:00 AM', '11:00 PM'),
(81, 'MovieMax Cinemas (Omaxe Mall).', 'Omaxe Mall, Rajpura Road,Patiala.', 'Rajpura Road', 'Patiala', '147001', 4, 600, ' 0175-5099000 ', 'info@Omaxe.com', '10:00 AM', '11:00 PM'),
(82, 'Balraj Surya Cinema', 'Near Old Bus Stand, GT Road,Patiala.', 'GT Road.', 'Patiala', '147001 ', 2, 300, ' 0175-2222000', 'info@Balrajsurya.com', '10:30 AM', '11:00 PM'),
(83, 'Malwa Cinema', ' Near Moti Bagh, Chandigarh Road ,Patiala.', 'Chandigarh Road.', 'Patiala', '147001 ', 2, 400, '0175-2211100', 'info@Malwacinema.com', '10:00 AM', '11:00 PM'),
(84, 'Phool Talkies.', ' Near Sadar Bazaar, GT Road, Patiala', 'GT Road.', 'Patiala', '147001 ', 1, 200, ' 0175-2222344', 'info@Phooltalkies.com', '10:00 AM', '11:00 PM'),
(85, 'JR Ohri Cinemas', 'Chandigarh Road, Magror, Rupnagar, Punjab.', 'Chandigarh Road.', 'Ropar', '140001', 4, 250, '+91 9875644542', 'info@JROhri.cinemas', '11:00 AM', '12:00 PM'),
(86, 'Smart Cinemaz.', 'Near J.S. Resort -1, New Garden Colony, Dashmesh Nagar, Rupnagar (Ropar), Punjab.', 'Dashmesh Nagar', 'Ropar', ' 140001', 3, 300, '+91 99148 01345', 'info@Smartcinemaz.com', '10:00 AM', '11:00 PM'),
(87, 'Salh Cinema.', 'Ramgarh Alias Manda, Morinda, Rupnagar District, Punjab.', 'Ramgarh Alias Manda.', 'Ropar', '140101', 1, 250, '+91 84378 18449', 'info@Salhcinema.com', '10:00 AM', '11:00 PM'),
(88, 'KBP Kalyan Talkies', 'Phool Chakkar, Ropar, Rupnagar, Punjab.', 'Phool Chakkar.', 'Ropar', '140001', 1, 250, '+91 9876754462', 'info@ Kalyan.com', '10:00 AM', '11: 00 PM'),
(89, 'Mukta A2 Cinemas ', '17 Marble Khasra No. 29/4, Rupnagar, Ropar.', 'Rupnagar.', 'Ropar', '140001 ', 2, 912, '+91 9867652671', 'info@Mukta.com', '10:00 AM', '11:00 PM'),
(90, 'Suncity Cinemas', 'Homeland City Mall, Sai Chakkan Road, Near Bhardwaj Hospital', 'Sai Chakkan Road.', 'Ropar', '140001', 2, 200, '+91 98570 29297', ' Suncity Cinemas', '10:00 AM', '11:00 PM'),
(91, 'PVR Cinemas (VR Punjab Mall).', ' NH-21, Chandigarh Kharar Road, Sector 118, Sahibzada Ajit Singh Nagar, Mohali, Punjab.', 'Sahibzada Ajit Singh Nagar.', 'Mohali', '160055', 9, 1, '+91-8800900009 ', 'cm.mohali@pvrcinemas.com', '10:00 AM', '10:00 PM'),
(92, 'Bassi Theater', 'Phase 2, Near Gian Jyoti Road, Sahibzada Ajit Singh Nagar, Mohali, Punjab.', 'Sahibzada Ajit Singh Nagar.', 'Mohali', '160055', 2, 2, '+91 9878655432', 'info@Bassitheater.com', '9:00 AM', '11:00 PM'),
(93, 'Bonzai 7D Adventure', ' NH-21, Chandigarh Kharar Road, Sector 118, Sahibzada Ajit Singh Nagar, Mohali, Punjab.', 'Sahibzada Ajit Singh Nagar.', 'Mohali', '160055', 5, 1, '+91 9161145429', 'bonzai7d.mohali@gmail.com', '11:00 AM', '10:00 PM'),
(94, 'PVR Cinemas LUXE (VR Punjab Mall).', 'NH-21, Chandigarh Kharar Road, Sector 118, Sahibzada Ajit Singh Nagar, Mohali, Punjab.', 'Sahibzada Ajit Singh Nagar.', 'Mohali', '160055', 9, 1, ' +91 8800900009 ', 'cm.mohali@pvrcinemas.com', '10:00 AM', '11:00 PM'),
(95, 'Cinepolis Cinemas ', ' Bestech Square Mall, Near Mohali Golf Range, Mohali.', 'Near Mohali Golf Range.', 'Mohali', '160059', 7, 1, '0172-5072222', 'info@Cinepoliscinemas.com', '10:00 AM', '11:00 PM'),
(96, 'Cinepolis Cinemas at TDI Mall', ' TDI Mall, TDI City, Sector 68, Mohali.', 'TDI City, Sector 68, Mohali.', 'Mohali', '160068', 3, 500, '+91 95822 29519', 'info@Cinepolis.com', '10:00 AM', '11:00 PM'),
(97, 'Piccadily Cinemas ', 'Piccadily Square Mall, Landran, Mohali, Punjab', 'Piccadily Square Mall.', 'Mohali', '140307', 5, 600, '+91 82878 88234', 'info@Piccadilycinemas ', '10:00 AM', '11:00 PM'),
(98, 'Neelam Theatre', 'Sector 17, Chandigarh, Mohali, Punjab', 'Chandigarh', 'Mohali', '160017', 1, 300, '+91 9784873774', 'info@Neelamtheatre.com', '10:00 AM', '11:00 PM'),
(99, 'Miraj Cinemas.', 'Sangrur Road, Near Bus Stand, Dhuri, Punjab', 'Sangrur Road.', 'Sangrur', '148024', 3, 300, '+91 9856767842', 'info@Mirajcinemas.com', '10:00 AM', '11:00 PM'),
(100, 'Heena Cinema', 'Barnala Rd, Agar Nagar, Malerkotla,', 'Barnala Rd.', 'Sangrur', '148023', 1, 200, '+91 95175 23365', 'info@Heenacinema.com', '10:00 AM', '11:00 PM'),
(101, 'Fun Square 5D Adventure', 'Village Akoi Sahib, Dhuri Road, Sangrur, Punjab.', 'Dhuri Road.', 'Sangrur', '148001', 2, 350, '+91 82838 23353', 'info@Funsquare5Dadventure.com', '10:00 AM', '11:00 PM'),
(102, 'SRS Cinemas', ' Malout Rd, opposite State Bank of India, S.A.S Nagar, Sri Muktsar Sahib, Punjab.', 'Sri Muktsar Sahib.', '{Sri Muktsar Sahib}', '152026', 3, 400, '+91 90410 18186', 'info@SRScinemas', '10:00 AM', '11:00 PM'),
(103, 'Sky Cine', '3rd Floor, Sky Mall & Shopping Complex, NH7, Bathinda Rd, Malout, Punjab.', ' Bathinda Rd', '{Sri Muktsar Sahib}', '152107', 3, 500, '+91 75270 34604', 'info@Skycine', '10:00 AM', '11:00 PM'),
(104, 'CCP Cineplex', ' City Crown Plaza, Muktsar Road, Near Pritam Palace, Malout, Punjab.', 'Muktsar Road.', '{Sri Muktsar Sahib}', '152107', 2, 300, '+91 9867643522', 'info@CCPcineplex.com', '12:00 AM', '12:00 PM'),
(105, 'Partap Cinema', 'Bohri Chownk, Tarn Taran Sahib, Punjab.', 'Tarn Taran Sahib.', '{Tarn Taran}', '143401', 3, 400, '099889 39668.', 'info@Partapcinema.com', '10:00 AM', '11:00 PM');

-- --------------------------------------------------------

--
-- Table structure for table `new_movies`
--

CREATE TABLE `new_movies` (
  `id` int(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `language` varchar(255) NOT NULL,
  `genres` varchar(255) NOT NULL,
  `date` date NOT NULL,
  `about` varchar(1000) NOT NULL,
  `trailer` varchar(255) NOT NULL,
  `rating` varchar(255) NOT NULL,
  `poster` varchar(255) NOT NULL,
  `time` varchar(255) NOT NULL,
  `banner` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `new_movies`
--

INSERT INTO `new_movies` (`id`, `name`, `language`, `genres`, `date`, `about`, `trailer`, `rating`, `poster`, `time`, `banner`) VALUES
(23, 'Kakuda', 'Hindi /  Malayalam', 'Action /  Drama /  Comedy', '2024-09-17', 'Kakuda is a horror-comedy starring Riteish Deshmukh, Sonakshi Sinha and Saqib Salem in prominent roles, It is directed by AdityaSarpotdar and produced by RonnieScrewvala..\n', 'Movies_Poster/Daaru Na Peenda Hove (Trailer).mp4', '8', 'Movies_Poster/kakuda.jpeg', '120', 'Movies_Poster/kakuda_banner.jpg'),
(24, 'Gandhi 3', 'Punjabi', 'Action /  Drama', '2024-09-17', 'A local guy named Garry was called Gandhi and some referred to him as Robinhood in Punjab. One day, Garry gets the chance to learn the true story of Gandhi`s life. As the tale unfolds, Garry undergoes a profound transformation, emerging as a completely changed person.\n', 'Movies_Poster/Daaru Na Peenda Hove (Trailer).mp4', '8', 'Movies_Poster/gandhi3_poster.jpeg', '143', 'Movies_Poster/gandhi3.jpg'),
(25, 'Bibi Rajni', 'Punjabi', 'Drama', '2024-08-30', 'Bibi Rajni is a Punjabi movie starring Roopi Gill, Yograj Singh, Gurpreet Ghuggi and Jass Bajwa in prominent roles. It is written and directed by Amar Hundal.\n\n', 'Movies_Poster/Daaru Na Peenda Hove (Trailer).mp4', '9.3', 'Movies_Poster/bibi_rajni_poster.jpeg', '142', 'Movies_Poster/bibi_rajni_banner.jpg'),
(26, 'Emergency', 'Hindi', 'Biography /  Drama /  Historical', '2024-09-06', 'Based on true events that unfolded in 1975. The chronicles incidents that took place under the leadership of Mrs Indira Gandhi, one of the most Powerful Women in Indian History.\n\n\n', 'Movies_Poster/Daaru Na Peenda Hove (Trailer).mp4', '7.5', 'Movies_Poster/emergency-indian-movie-poster.jpg', '146', 'Movies_Poster/WhatsApp Image 2023-06-24 at 12.34.01 PM.jpeg');

-- --------------------------------------------------------

--
-- Table structure for table `registeruser`
--

CREATE TABLE `registeruser` (
  `Id` int(255) NOT NULL,
  `Name` varchar(255) DEFAULT NULL,
  `Email` varchar(255) DEFAULT NULL,
  `Phone` varchar(255) DEFAULT NULL,
  `Password` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `registeruser`
--

INSERT INTO `registeruser` (`Id`, `Name`, `Email`, `Phone`, `Password`) VALUES
(6, 'Amandeep kaur', 'aman@gmail.com', '9878279940', '@_Aman31'),
(7, 'sandeep singh', 's@gmail.com', '7719427838', '@_Sandeep81'),
(8, 'Disha', 'Disharani84@gmail.com', '9882539985', '@_Disha123'),
(9, 'Ajeetsingh', 'Singhjeet@gmail.com', '9878934672', '@_Ajeet672'),
(10, 'Gurkiran kaur', 'Kaurkiran@gmail.com', '9844563733', '@_Gurkaur33'),
(11, 'Gurkiran kaur', 'Kaurkiran@gmail.com', '9844563733', '@_Gurkaur33'),
(12, 'Balvinder singh', 'B.vinder@gmail.com', '9875544345', '@SinghVinder45'),
(13, 'Gurleen kumari', 'G.kumari@gmail.com', '9877635224', 'Leen@_224'),
(14, 'Arjan Singh', 'Singharjan@gmail.com', '8647353767', 'Arjan_767'),
(15, 'Agampreet kaur', 'Agampreet02@gmail.com', '9823546774', '@_Agam774'),
(16, 'Jasleen kuar', 'Jasleen08@gmail.com', '9889763446', 'Jass_kaur446'),
(17, 'Sarbjit Singh', 'Sarbjit.09@gmail.com', '9867463443', 'Singh@_1998');

-- --------------------------------------------------------

--
-- Table structure for table `upcoming_movies`
--

CREATE TABLE `upcoming_movies` (
  `id` int(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `language` varchar(255) NOT NULL,
  `genres` varchar(255) NOT NULL,
  `date` date NOT NULL,
  `about` varchar(255) NOT NULL,
  `trailer` varchar(255) NOT NULL,
  `poster` varchar(255) NOT NULL,
  `time` int(255) NOT NULL,
  `banner` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `upcoming_movies`
--

INSERT INTO `upcoming_movies` (`id`, `name`, `language`, `genres`, `date`, `about`, `trailer`, `poster`, `time`, `banner`) VALUES
(8, 'Ardaas Sarbat de Bhale di', 'Punjabi', 'Drama /  Family', '2024-10-04', 'Actor and comedian Gurpreet Ghuggi added, \"Ardaas Sarbat De Bhale Di is Punjabi, but its thought is universal. It does not belong to any one religious sect or any country. It\'s about praying for the good of all. The movie shares many life lessons, reflect', 'Movies_Poster/Daaru Na Peenda Hove (Trailer).mp4', 'Movies_Poster/ardaas sarbat de bhalle di banner.jpeg', 135, 'Movies_Poster/Ardaas sarbat de bhale di trailer.jpg'),
(9, 'Sucha Soorma', 'Punjabi', 'Drama', '2024-09-20', 'Sucha Soorma, a much-anticipated film, is all set to grace the silver screens across the globe on 20th September 2024. The grandeur of this film is a must-have experience in theatres. Sucha Soorma is presented by Saga Studios in association with Seven Col', 'Movies_Poster/Daaru Na Peenda Hove (Trailer).mp4', 'Movies_Poster/sucha soorma pics.jpeg', 136, 'Movies_Poster/sucha soorma banner.jpeg'),
(10, 'Binny And Family', 'Hindi', 'Comedy /  Drama /  Family', '2024-09-20', 'Binny (Anjini Dhawan), a rebellious teenager, lives in London alongwith her conservative grandfather (Pankaj Kapur) from a small town in Bihar. Needless to say, the two are poles apart and don\'t agree on anything. But what happens when a dramatic incident', 'Movies_Poster/Daaru Na Peenda Hove (Trailer).mp4', 'Movies_Poster/binny and family 2.jpeg', 140, 'Movies_Poster/Binny-and-Family-banner.jpeg'),
(11, 'Kahan Shuru Khatam', 'Hindi', 'Drama /  Comedy /  Romantic', '2024-09-20', 'Kahan Shuru Kahan Khatam is an upcoming Indian Hindi-language romantic comedy film, written by Laxman Utekar and Rishi Virmani, and directed by Saurabh Dasgupta. The film stars Dhvani Bhanushali and Aashim Gulati in the lead roles.\n', 'Movies_Poster/Daaru Na Peenda Hove (Trailer).mp4', 'Movies_Poster/photos.jpg', 136, 'Movies_Poster/kahan_Shuru_kahan_khatam_banner.jpg'),
(12, 'Adbhut', 'Hindi', 'Drama /  Thiller /  Horror', '2024-09-15', 'Adbhut is Hindi movie. The movie is directed by Sabbir Khan and will feature Nawazuddin Siddiqui, Diana Penty, Shreya Dhanwanthary and Rohan Mehra as lead characters.\n\n\n', 'Movies_Poster/Daaru Na Peenda Hove (Trailer).mp4', 'Movies_Poster/download.jfif', 122, 'Movies_Poster/New-poster-of-Nawazuddin-Siddiquis-horror-thriller-Adbhut-unveiled-set-to-release-on-Sony-Max-on-September-15-2-354x199.jpg'),
(13, 'Shukrana', 'Punjabi', 'Drama /  Family', '2024-09-27', 'shukrana movie , Directed by Simerjit Singh, the film stars Neeru Bajwa, Jass Bajwa, Amrit Maan, and B.N. Sharma. The plot revolves around Veeran, who faces family pressure to marry her late husband\'s brother after the sudden death of her husband, Jeaona.', 'Movies_Poster/Daaru Na Peenda Hove (Trailer).mp4', 'Movies_Poster/shukrana poster.jpg', 136, 'Movies_Poster/shukrana movie banner.jpg'),
(14, 'Shahkot', 'Punjabi', 'Drama', '2024-10-04', 'Iqbal Singh, a determined Punjabi youth who decides to pursue his passion of venturing abroad, only for his life to take an unexpected turn\n', 'Movies_Poster/Daaru Na Peenda Hove (Trailer).mp4', 'Movies_Poster/shakot 2.jpg', 135, 'Movies_Poster/Guru.webp');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `admin`
--
ALTER TABLE `admin`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `booking`
--
ALTER TABLE `booking`
  ADD PRIMARY KEY (`booking_id`);

--
-- Indexes for table `cast`
--
ALTER TABLE `cast`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `cinemas`
--
ALTER TABLE `cinemas`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `new_movies`
--
ALTER TABLE `new_movies`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `registeruser`
--
ALTER TABLE `registeruser`
  ADD PRIMARY KEY (`Id`);

--
-- Indexes for table `upcoming_movies`
--
ALTER TABLE `upcoming_movies`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `admin`
--
ALTER TABLE `admin`
  MODIFY `id` int(255) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `cast`
--
ALTER TABLE `cast`
  MODIFY `id` int(255) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=55;

--
-- AUTO_INCREMENT for table `cinemas`
--
ALTER TABLE `cinemas`
  MODIFY `id` int(255) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=106;

--
-- AUTO_INCREMENT for table `new_movies`
--
ALTER TABLE `new_movies`
  MODIFY `id` int(255) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=27;

--
-- AUTO_INCREMENT for table `registeruser`
--
ALTER TABLE `registeruser`
  MODIFY `Id` int(255) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=18;

--
-- AUTO_INCREMENT for table `upcoming_movies`
--
ALTER TABLE `upcoming_movies`
  MODIFY `id` int(255) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
