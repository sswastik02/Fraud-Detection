export const token_key = 'E_COMMERCE_TOKEN'
export const user_id = 'USER_ID'
export const setToken = token => {
  window.localStorage.setItem(token_key, token)
}

export const setId = id => {
  window.localStorage.setItem(user_id, id)
}

export const getToken = () => {
  let token = window.localStorage.getItem(token_key)
  if (!!token) return token
  return false
}


export const isLogin = () => {
  if (!!getToken()) {
    return true
  }
  return false
}

export const logout = () => {
  window.localStorage.clear()
}
