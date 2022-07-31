import './HomeScreen.css'
import {useEffect} from 'react'
import {useDispatch, useSelector} from 'react-redux'
import axios from 'axios'

// Components
import Product from '../components/Product'

//Actions
import {getProducts as listProducts} from '../redux/actions/productActions'
import {setUserDeatils} from '../redux/actions/userAction'

const HomeScreen = () => {
  const dispatch = useDispatch()
  const url = 'https://www.google.com/'
  const getProducts = useSelector(state => state.getProducts)
  const {products, loading, error} = getProducts

  useEffect(() => {
    dispatch(listProducts())
  }, [dispatch])

  useEffect(() => {
    dispatch(setUserDeatils())
  }, [dispatch])

  const handleClick = async () => {
    await axios
      .post("http://127.0.0.1:8000/api/phishingurl/detect", {
        url:url
        
      })
      .then((res) => {
        console.log(res.data.phishing);
        if(res.data.phishing ===true ) alert('Phishing Website')
        else alert('Non-fraudulent website')
        console.log(res);
        
      })

      .catch((err) => console.log(err));

      
  };

  
  return (
    <div className="homescreen">
      <h2 className="homescreen__title">Latest Products</h2>
      <div className="homescreen__products">
        {loading ? (
          <h2>Loading...</h2>
        ) : error ? (
          <h2>{error}</h2>
        ) : (
          products.map(product => (
            <Product
              key={product._id}
              name={product.name}
              description={product.description}
              price={product.price}
              imageUrl={product.imageUrl}
              productId={product._id}
            />
          ))
        )}
        <div>
          AD 
          <a onClick={handleClick}>
             <img src='https://static-prod.adweek.com/wp-content/uploads/2019/12/hulu-cheez-it-ad-CONTENT-2019.jpg'/>
          </a>
        </div>
      </div>
    </div>
  )
}

export default HomeScreen
