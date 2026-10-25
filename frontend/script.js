let chat = document.querySelector('.chat');
let input = document.getElementById('messageInput');
let button = document.getElementById('sendButton');

button.addEventListener("click",function()
{
  let text = input.value.trim();//获取文字
  if(text =="") return;//判断是否为空
  
  //创建div
  let message = document.createElement('div');
  message.className = 'userMessage';

  //消息内容
  let p = document.createElement('p');
  p.innerText = text;

  message.appendChild(p);
  chat.appendChild(message);
  input.value = "";

  chat.scrollTop = chat.scrollHeight;
});