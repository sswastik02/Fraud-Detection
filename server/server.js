
require('dotenv').config()
const express = require('express')
const productRoutes = require('./routes/productRoutes')
const userRoutes = require('./routes/userRoutes')
const cartRoutes = require('./routes/cartRoutes')
const userinfoRoutes = require('./routes/userinfoRoutes')
const aadharinfoRoutes = require('./routes/aadharinfoRoutes')
const {connectDB} = require('./config/db')
const cors = require('cors')

connectDB()

const app = express()

app.use(express.json())
app.use(cors())



app.get('/', (req, res) => {
  res.json({message: 'API running...'})
})

app.use('/api/products', productRoutes)
app.use('/api/user', userRoutes)
app.use('/api/cart', cartRoutes)
app.use('/api/userinfo', userinfoRoutes )
app.use('/api/aadharinfo' , aadharinfoRoutes)

const PORT =5000
app.listen(PORT, () => console.log(`Server running on port ${PORT}`))
