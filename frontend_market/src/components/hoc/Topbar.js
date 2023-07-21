import React, { useEffect } from "react";
import bobby from 'assets/bobby.jpg'
function Topbar() {
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
    <div className="topbar">
      <div className="inputBox">
        <input type="text" placeholder="What do you need?" />
        <i class="fa fa-search" aria-hidden="true"></i>
      </div>

      <div className="profileContainer">
      <i class="fa fa-bell" aria-hidden="true"></i>

        <div className="profileImage">
          <img src={bobby} alt="bobbygames" />
        </div>
        <p className="profileName">Bobby Gamer</p>
        <i class="fa fa-chevron-down" aria-hidden="true"></i>


        {/* <div className="menuContainer" id="menuContainer">
          <ul>
            <li>Web design</li>
            <li>UI / UX</li>
            <li>Form Design</li>
            <li>UI design</li>
          </ul>
        </div> */}
      </div>
    </div>
  );
}

export default Topbar;