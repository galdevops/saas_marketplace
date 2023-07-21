import React, { useEffect } from "react";
import bobby from 'assets/bobby.jpg'
function Footer() {
//   useEffect(() => {
//     const mouseTarget = document.getElementById("menuChevron");
//     const menuContainer = document.getElementById("menuContainer");
//     mouseTarget.addEventListener("mouseenter", () => {
//       mouseTarget.style.transform = "rotate(180deg)";
//       menuContainer.style.transform = "translateX(0px)";
//     });

//     menuContainer.addEventListener("mouseleave", () => {
//       mouseTarget.style.transform = "rotate(0deg)";
//       menuContainer.style.transform = "translateX(300px)";
//     });
//   }, []);

  return (
    <div id="footer">
        <div className="site-footer">
        <div className="footer-logo">
          <span>
            <img src={bobby} alt="bobbygames" />
          </span>
          <p>@BobbyGames 2023</p>
        </div>
        <div className="footer-icons">
        <div><i className="fa fa-envelope" aria-hidden="true"></i></div>
        <div><i class="fa fa-gamepad"></i></div>
        </div>
        
        

        </div>
      
    </div>
  );
}

export default Footer;