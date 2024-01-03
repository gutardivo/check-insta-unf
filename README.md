# Check Instagram Unfollowers

### First Step
Open your profile and go to following, then scroll down until you load all usernames (you will know when it stops showing loading icon)

### Second Step
Open console on your browser, you can find it in developer tools in Safari, and right click and inspecting element in Chrome

### Third Step

Paste this in console: 

_NOTE: Class_ _"__ap3a" may change, if it is not working, check the first class name in username element and change it in code_

```
arr = []
for (let i=0;i<document.getElementsByClassName("_ap3a").length;i++) {
  let username = document.getElementsByClassName("_ap3a")[i].innerText
    if(username !=="Following" && username !=="Follow" && username !=="Remove") { arr.push(username) }
}
console.log(arr)
```

Then get all the elements in JSON format and paste it in python code

Repeat the same for followers and run the code
