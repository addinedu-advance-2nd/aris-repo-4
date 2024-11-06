// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from robot_msgs:msg/UserOrder.idl
// generated code does not contain a copyright notice
#include "robot_msgs/msg/detail/user_order__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"


// Include directives for member types
// Member `action`
// Member `icecream`
// Member `topping`
// Member `topping_type`
#include "rosidl_runtime_c/string_functions.h"

bool
robot_msgs__msg__UserOrder__init(robot_msgs__msg__UserOrder * msg)
{
  if (!msg) {
    return false;
  }
  // action
  if (!rosidl_runtime_c__String__init(&msg->action)) {
    robot_msgs__msg__UserOrder__fini(msg);
    return false;
  }
  // icecream
  if (!rosidl_runtime_c__String__init(&msg->icecream)) {
    robot_msgs__msg__UserOrder__fini(msg);
    return false;
  }
  // topping
  if (!rosidl_runtime_c__String__init(&msg->topping)) {
    robot_msgs__msg__UserOrder__fini(msg);
    return false;
  }
  // topping_type
  if (!rosidl_runtime_c__String__init(&msg->topping_type)) {
    robot_msgs__msg__UserOrder__fini(msg);
    return false;
  }
  return true;
}

void
robot_msgs__msg__UserOrder__fini(robot_msgs__msg__UserOrder * msg)
{
  if (!msg) {
    return;
  }
  // action
  rosidl_runtime_c__String__fini(&msg->action);
  // icecream
  rosidl_runtime_c__String__fini(&msg->icecream);
  // topping
  rosidl_runtime_c__String__fini(&msg->topping);
  // topping_type
  rosidl_runtime_c__String__fini(&msg->topping_type);
}

bool
robot_msgs__msg__UserOrder__are_equal(const robot_msgs__msg__UserOrder * lhs, const robot_msgs__msg__UserOrder * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // action
  if (!rosidl_runtime_c__String__are_equal(
      &(lhs->action), &(rhs->action)))
  {
    return false;
  }
  // icecream
  if (!rosidl_runtime_c__String__are_equal(
      &(lhs->icecream), &(rhs->icecream)))
  {
    return false;
  }
  // topping
  if (!rosidl_runtime_c__String__are_equal(
      &(lhs->topping), &(rhs->topping)))
  {
    return false;
  }
  // topping_type
  if (!rosidl_runtime_c__String__are_equal(
      &(lhs->topping_type), &(rhs->topping_type)))
  {
    return false;
  }
  return true;
}

bool
robot_msgs__msg__UserOrder__copy(
  const robot_msgs__msg__UserOrder * input,
  robot_msgs__msg__UserOrder * output)
{
  if (!input || !output) {
    return false;
  }
  // action
  if (!rosidl_runtime_c__String__copy(
      &(input->action), &(output->action)))
  {
    return false;
  }
  // icecream
  if (!rosidl_runtime_c__String__copy(
      &(input->icecream), &(output->icecream)))
  {
    return false;
  }
  // topping
  if (!rosidl_runtime_c__String__copy(
      &(input->topping), &(output->topping)))
  {
    return false;
  }
  // topping_type
  if (!rosidl_runtime_c__String__copy(
      &(input->topping_type), &(output->topping_type)))
  {
    return false;
  }
  return true;
}

robot_msgs__msg__UserOrder *
robot_msgs__msg__UserOrder__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  robot_msgs__msg__UserOrder * msg = (robot_msgs__msg__UserOrder *)allocator.allocate(sizeof(robot_msgs__msg__UserOrder), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(robot_msgs__msg__UserOrder));
  bool success = robot_msgs__msg__UserOrder__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
robot_msgs__msg__UserOrder__destroy(robot_msgs__msg__UserOrder * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    robot_msgs__msg__UserOrder__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
robot_msgs__msg__UserOrder__Sequence__init(robot_msgs__msg__UserOrder__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  robot_msgs__msg__UserOrder * data = NULL;

  if (size) {
    data = (robot_msgs__msg__UserOrder *)allocator.zero_allocate(size, sizeof(robot_msgs__msg__UserOrder), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = robot_msgs__msg__UserOrder__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        robot_msgs__msg__UserOrder__fini(&data[i - 1]);
      }
      allocator.deallocate(data, allocator.state);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
robot_msgs__msg__UserOrder__Sequence__fini(robot_msgs__msg__UserOrder__Sequence * array)
{
  if (!array) {
    return;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();

  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      robot_msgs__msg__UserOrder__fini(&array->data[i]);
    }
    allocator.deallocate(array->data, allocator.state);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

robot_msgs__msg__UserOrder__Sequence *
robot_msgs__msg__UserOrder__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  robot_msgs__msg__UserOrder__Sequence * array = (robot_msgs__msg__UserOrder__Sequence *)allocator.allocate(sizeof(robot_msgs__msg__UserOrder__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = robot_msgs__msg__UserOrder__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
robot_msgs__msg__UserOrder__Sequence__destroy(robot_msgs__msg__UserOrder__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    robot_msgs__msg__UserOrder__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
robot_msgs__msg__UserOrder__Sequence__are_equal(const robot_msgs__msg__UserOrder__Sequence * lhs, const robot_msgs__msg__UserOrder__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!robot_msgs__msg__UserOrder__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
robot_msgs__msg__UserOrder__Sequence__copy(
  const robot_msgs__msg__UserOrder__Sequence * input,
  robot_msgs__msg__UserOrder__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(robot_msgs__msg__UserOrder);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    robot_msgs__msg__UserOrder * data =
      (robot_msgs__msg__UserOrder *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!robot_msgs__msg__UserOrder__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          robot_msgs__msg__UserOrder__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!robot_msgs__msg__UserOrder__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
