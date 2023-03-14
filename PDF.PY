import pdfkit  

def make_pdf(_string):
  try:
    pdfkit.from_string(my_string,'output.pdf')
  except:
    pass
   

my_string='''<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <meta name="description" content="Ecommerce website" />
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.9.1/font/bootstrap-icons.css" />
  <title>E-COMMERCE</title>
  <link rel="stylesheet" href="index.css" />
</head>

<body>
  <nav>
    <div class="nav-cont">
      <h3 class="nav-logo">E Commerce</h3>
      <div class="cart-cont">
        <i class="bi-bag cart-icon"></i>
        <span class="cart-count">9+</span>
      </div>
    </div>
  </nav>
  <header>
    <!----- added by ajmal on header poster ---->
    <div class="poster">
      <h3 class="device_name">Loremsd</h3>
      <h2 class="wireless">Lorem.</h2>
      <h1 class="device_variant">Lorem ipsusfda</h1>

      <img src="https://cdn.sanity.io/images/kyml1h03/production/a205aaa5ac2c75342801e683c3b78ea2fff8913b-600x600.webp"
        alt="" class="product_pic" />
      <div class="desc_details">
        <button id="click_to_buy">Shop Wireless Headphones</button>
        <article class="desc_Card">
          <h3 class="descript">Lorem.</h3>
          <p class="description">
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Quas sint
            ea sapiente, atque nihil eius quisquam optio libero, quasi
            
          </p>
        </article>
      </div>
    </div>
  </header>

  <main>
    <h2 class="text-center main-title">Top Recommended Products</h2>
    <h5 class="text-center main-subtitle">These are some of the users' most popular picks</h5>
    <div class="prod-list">
      <div class="prod-card card-shadow">
        <a><img src="" alt="" /></a>
        <div class="prod-footer">
          <h3>Lorem, ipsum dolor.</h3>
          <h3>Price</h3>
        </div>
      </div>
      <div class="prod-card card-shadow">
        <a><img src="" alt="" /></a>
        <div class="prod-footer">
          <h3>Lorem, ipsum dolor.</h3>
          <h3>Price</h3>
        </div>
      </div>
      <div class="prod-card card-shadow">
        <a><img src="" alt="" /></a>
        <div class="prod-footer">
          <h3>Lorem, ipsum dolor.</h3>
          <h3>Price</h3>
        </div>
      </div>
      <div class="prod-card card-shadow">
        <a><img src="" alt="" /></a>
        <div class="prod-footer">
          <h3>Lorem, ipsum dolor.</h3>
          <h3>Price</h3>
        </div>
      </div>
      <div class="prod-card card-shadow">
        <a><img src="" alt="" /></a>
        <div class="prod-footer">
          <h3>Lorem, ipsum dolor.</h3>
          <h3>Price</h3>
        </div>
      </div>
      <div class="prod-card card-shadow">
        <a><img src="" alt="" /></a>
        <div class="prod-footer">
          <h3>Lorem, ipsum dolor.</h3>
          <h3>Price</h3>
        </div>
      </div>
      <div class="prod-card card-shadow">
        <a><img src="" alt="" /></a>
        <div class="prod-footer">
          <h3>Lorem, ipsum dolor.</h3>
          <h3>Price</h3>
        </div>
      </div>
      <div class="prod-card card-shadow">
        <a><img src="" alt="" /></a>
        <div class="prod-footer">
          <h3>Lorem, ipsum dolor.</h3>
          <h3>Price</h3>
        </div>
      </div>
      <div class="prod-card card-shadow">
        <a><img src="" alt="" /></a>
        <div class="prod-footer">
          <h3>Lorem, ipsum dolor.</h3>
          <h3>Price</h3>
        </div>
      </div>
      <div class="prod-card card-shadow">
        <a><img src="" alt="" /></a>
        <div class="prod-footer">
          <h3>Lorem, ipsum dolor.</h3>
          <h3>Price</h3>
        </div>
      </div>
      <div class="prod-card card-shadow">
        <a><img src="" alt="" /></a>
        <div class="prod-footer">
          <h3>Lorem, ipsum dolor.</h3>
          <h3>Price</h3>
        </div>
      </div>
      <div class="prod-card card-shadow">
        <a><img src="" alt="" /></a>
        <div class="prod-footer">
          <h3>Lorem, ipsum dolor.</h3>
          <h3>Price</h3>
        </div>
      </div>
     
    </div>
  </main>
  <footer>
    <div class="footer_poster">
      <div class="tag">
        <h4>29% OFF</h4>
        <h2 class="acronouns">Fine<br>Smile</h2>
        <h4>&nbsp;&nbsp;29 Apr to 29 may</h4>
        <img src="https://cdn.sanity.io/images/kyml1h03/production/a64b345016e96adfb8849af5521c8e0ecfe8f027-555x555.webp"
          class="footer_pic" alt="headphones">
      </div>
      <div class="shop_now">
        <h4>Beats Solo Air</h4>
        <h1> Summer<br> Sale</h1>
        <p class="descpt">company that's grown from 270 to 480 employees in the last 12 months</p>
        <button id="click_to_shop">Shop now</button>
      </div>
    </div>
    <p class="footer-copyright text-center">2022 E Commerce Store All Rights Reserved</p>
    <div class="footer-links text-center">
      <i class="footer-icon bi-instagram"></i>
      <i class="footer-icon  bi-twitter"></i>
      <i class="footer-icon  bi-facebook"></i>
    </div>
  </footer>
  
  <style>
  
  * {
  padding: 0;
  margin: 0;
  box-sizing: border-box;
}

/* variables */
:root {
  --bp-sm: 576px;
  --bp-md: 768px;
  --bp-lg: 992px;
  --bp-xl: 1200px;
  --bp-xxl: 1400px;
}

/* utility classes */
.text-center {
  text-align: center;
}

.text-disabled {
  opacity: 0.7;
}

html {
  /* initial font size for rem units */
  font-size: 22px;
}

nav {
  width: 100% !important;
  padding: 1em 0;
}

.nav-cont {
  display: flex;
  width: 100%;
  justify-content: space-between;
  padding: 0 2em;
  max-width: var(--bp-xl);
  margin: 0 auto;
}

.nav-logo {
  font-size: 1.5em;
}

.cart-cont {
  position: relative;
}

.cart-icon {
  font-size: 1.2em;
}

.cart-count {
  position: absolute;
  transform: translate(0.6em, -0.4em);
  top: 0;
  right: 0;
  background-color: red;
  border-radius: 50%;
  padding: 3px;
  font-weight: bold;
  font-size: 0.6em;
  color: #dcdcdc;
}

header {
  width: 100% !important;
  padding: 0 1em;
}

.poster {
  width: 100%;
  max-width: 1200px;
  background-color: #dcdcdc;
  margin-top: 0;
  padding: 1em 0;
  margin: 0 auto;
  border-radius: 25px;
  position: relative;
}

.product_title {
  position: relative;
}

.device_name {
  position: inherit;
  margin-top: 5%;
  margin-left: 2%;
  font-size: 28px;
  font-weight: 200;
}

.desc_details {
  display: flex;
  align-items: flex-start;
  justify-content: space-between;
}

article {
  z-index: 4;
  gap: 12%;
  width: 27%;
  display: grid;
  align-items: center;

  margin-right: 3%;
  margin-top: 0.5%;
}

#click_to_buy {
  margin-top: 1%;
  margin-left: 3%;
  border-radius: 10px;
  background-color: red;
  color: white;
  width: 30%;
  border-color: transparent;

  font-size: 100%;
  padding: 0.7%;
}

.product_pic {
  position: absolute;
  top: -1em;
  right: 0;
  width: 45%;
  margin-right: 2em;
  animation: bounce infinite 4s;
  z-index: 2;
}

@keyframes bounce {
  0%,
  100% {
    transform: translateY(0);
    transition-timing-function: ease-in;
  }
  50% {
    transform: translateY(-15px);
    transition-timing-function: ease-out;
  }
}

.device_variant {
  color: white;
  font-weight: 700;
  font-size:min(12vw,8rem);
  text-align: center;
  overflow: hidden;
}

.wireless {
  margin-left: 2%;
  margin-bottom: -10px;
  font-size: 75px;
}

.description {
  font-weight: 5;
  font-style: normal;
  font-family: sans-serif;
  font-size: 14px;
  line-height: 19px;
}

.descript {
  font-size: 24px;
  font-weight: 600;
}

.box {
  width: 120px;
  height: 120px;
  border: 1px solid;
  float: left;
}

.footer_poster {

  background-color: rgb(252, 10, 10);
  padding: 1rem;
  height: 25rem;
  width: 70%;
  margin-left: 5%;
  position: relative;
  border-radius: 12px;
  color: white;
  z-index: 1;
  box-shadow: -2px 5px 8px 3px rgb(110, 108, 108);

  margin-bottom: 2rem;
  margin-left: 12%;

}

.footer_pic {

  position: absolute;
  top: 0.8rem;
  right: 0;
  width: 50%;
  margin-right: -1rem;
  animation: bounce infinite 4s;
  z-index: 2;


}

h4 {

  font-size: 0.8rem;

}

.descpt {
  font-size: 1rem;
}

.acronouns {
  font-size: 2.5rem;
}

h1 {
  font-size: 2.5rem;

}

#click_to_shop {
  width: 50%;
  margin-top: 0.90rem;
  font-size: 1.1rem;
  height: 1.8rem;
  border-radius: 20px;
  border: red solid;
  background-color: white;
  color: red;
}
@media only screen and (max-width: 600px) {
  nav {
    width: 100% !important;
    padding: 1em 0;
  }

  .nav-cont {
    display: flex;
    width: 100%;
    justify-content: space-between;
    padding: 0 2em;
  }

  .nav-logo {
    font-size: 1.5em;
  }

  .cart-cont {
    position: relative;
  }

  .cart-icon {
    font-size: 1.2em;
  }

  .cart-count {
    position: absolute;
    transform: translate(0.6em, -0.4em);
    top: 0;
    right: 0;
    background-color: red;
    border-radius: 50%;
    padding: 3px;
    font-weight: bold;
    font-size: 0.6em;
    color: #dcdcdc;
  }

  header {
    width: 100% !important;
    padding: 0 1em;
  }

  .poster {
    width: 100%;

    background-color: #dcdcdc;
    margin-top: 0;
    padding: 1em 0;
    margin: 0 auto;
    border-radius: 25px;
    position: relative;
    
  }

  .product_title {
    position: relative;
  }

  .device_name {
    position: inherit;
    margin-top: 5%;
    margin-left: 2%;
    font-size: 24px;
    font-weight: 200;
  }

  .desc_details {
    display: flex;
    align-items: flex-start;
    
    flex-direction: column-reverse;
    justify-content: space-between;
  }

  .desc_Card{
    z-index: 4;
    gap: 10%;
    width: 100%;
    display: grid;
    align-items: center;
      padding-left:2%;
    margin-right: 0%;
    margin-top: 2%;
  }

  #click_to_buy {
    margin-top: 5%;
    margin-left: 3%;
    border-radius: 10px;
    background-color: red;
    color: white;
    font-weight: bold;
    width: 70%;
    border-color: transparent;

    font-size: 14px;
  
    padding: 2.3%;
  }

  .product_pic {
    position: absolute;
    top: 10%;
    right: 4%;
    width: 84%;
    margin-right: -18%;
    animation: bounce infinite 4s;
    z-index: 2;
  }

  @keyframes bounce {
    0%,
    100% {
      transform: translateY(0);
      transition-timing-function: ease-in;
    }
    50% {
      transform: translateY(-15px);
      transition-timing-function: ease-out;
    }
  }

  .device_variant {
    color: white;
    margin-left: -2%;
    font-weight: 700;
    font-size: 4.5 em;
    overflow: hidden;
  }

  .wireless {
    margin-left: 2%;
    margin-bottom: -10px;
    font-size: 75px;
  }

  .description {
    font-weight: 100;
    font-style: normal;
    font-family: sans-serif;
    font-size: 13px;
 
    
  }

  .descript {
    font-size: 24px;
    margin-left: 1%;
    font-weight: 600;
  }

  .box {
    width: 120px;
    height: 120px;
    border: 1px solid;
    float: left;
  }

        .footer_poster {
    
          background-color: rgb(252, 10, 10);
          padding: 1rem;
          height: 80%;
          width: 90%;
          margin-left: 5%;
          position: relative;
          border-radius: 12px;
          color: white;
          z-index: 1;
          box-shadow: -2px 5px 8px 3px rgb(110, 108, 108);
    
          margin-bottom: 2rem;
    
        }
    
        .footer_pic {
    
          position: absolute;
          top: 0.8rem;
          right: 0;
          width: 80%;
          margin-right: -1rem;
          animation: bounce infinite 4s;
          z-index: 2;
    
    
        }
    
        h4 {
    
          font-size: 0.8rem;
    
        }
    
        .descpt {
          font-size: 1rem;
        }
    
        .acronouns {
          font-size: 2.5rem;
        }
    
        h1 {
          font-size: 2.5rem;
    
        }
    
        #click_to_shop {
          width: 50%;
          margin-top: 0.90rem;
          font-size: 1.1rem;
          height: 1.8rem;
          border-radius: 20px;
          border: red solid;
          background-color: white;
          color: red;
        }

  .footer_poster{

background-color: rgb(252, 10, 10);
  padding: 1rem;
  height: 22rem;
  width: 18.5rem;
  margin-left: 1.3rem;
  position: relative;
  border-radius: 12px;
  color: white;
  z-index: 1;



  }
  .footer_pic{
    
  position: absolute;
    top: 0.8rem;
    right: 0;
    width: 80%;
    margin-right: -1rem;
    animation: bounce infinite 4s;
    z-index: 2;
  
    
  }
  h4{

font-size: 0.8rem;

  }
  .descpt{
    font-size: 1rem;
  }
  .acronouns{
    font-size: 2.5rem;
  }
  h1{
    font-size: 2.5rem;

  }
  #click_to_shop{
  width: 50%;
  margin-top: 0.90rem;
   font-size: 1.1rem;
  height: 1.8rem;
  border-radius: 20px;
   border: red solid;
   background-color: white;
   color: red;
  }

}

/* for product list */

main {
  padding: 2rem 1rem;
  width: 100% !important;
}

.main-title {
  font-size: 2rem;
  margin: 0.3rem auto;
}

.main-subtitle {
  font-size: 1rem;
}

.prod-list {
  display: grid;
  gap: 1.5em;
  max-width: var(--bp-xl);
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  margin: 1rem auto;
}

.prod-card {
  background-color: aqua;
  padding: 1rem;
  height: 15rem;
}

footer {
  width: 100% !important;

}

.footer-copyright,
.footer-links {
  max-width: var(--bp-lg);
  margin: 0.3rem auto;
}


.card-shadow{
  box-shadow: rgba(0, 0, 0, 0.19) 0px 10px 20px, rgba(0, 0, 0, 0.23) 0px 6px 6px;
}

  
  
  </style>
</body>

</html>'''      
    # configuring pdfkit to point to our installation of wkhtmltopdf  

      
    # converting url to pdf file  
make_pdf(my_string)