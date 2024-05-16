const chatButton = document.querySelector('.chatbox__button');
const chatContent = document.querySelector('.chatbox__support');
const icons = {
    isClicked: '<img style="height:35px; width:35px;" src="../static/images/icons/clogo.png" />',
    isNotClicked: '<img style="height:35px; width:35px;" src="../static/images/icons/clogo.png" />'
}
const chatbox = new InteractiveChatbox(chatButton, chatContent, icons);
chatbox.display();
chatbox.toggleIcon(false, chatButton);