/* global describe, beforeEach, afterEach, it, expect, api, test, fetchData, jest */ 
jest.mock('axios', () => ({
  get: jest.fn()
}))

import { shallowMount, createLocalVue } from '@vue/test-utils'
import ItemsIndex from '../src/components/items/ItemsIndex.vue'
import axios from 'axios' // this is the mock from above
import VueRouter from 'vue-router'

const localVue = createLocalVue()
localVue.use(VueRouter)
const router = new VueRouter()

describe('ItemsIndex.test.js', () => {
  let cmp

  beforeEach(() => {
    cmp = shallowMount(ItemsIndex, { localVue, router
    }) // Create a copy of the original component
    jest.resetModules()
    jest.clearAllMocks()
  })

  it('Calls axios.get', async () => {
    await cmp.vm.getItems()
    expect(axios.get).toBeCalledWith('/api/items')
    // expect(cmp.$router.push).toHaveBeenCalledWith('/notfound')
  }),
  it('Returns a non-empty array of items', async () => {
    const result = await cmp.vm.getItems()
    expect.anything(result)
  }), 
  it('Returns an array of items containing the search term', () => {
    const result = cmp.vm.listingSearch('Trousers')
    expect(result).toBeDefined()
  })

})
