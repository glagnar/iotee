var number = parseFloat(msg.payload)

if (number > 20) {
    msg.payload = "red"
} else {
    msg.payload = "blue"
}

return msg;