// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from robot_msgs:msg/RobotState.idl
// generated code does not contain a copyright notice
#include "robot_msgs/msg/detail/robot_state__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"


// Include directives for member types
// Member `angles`
// Member `positions`
// Member `temperatures`
#include "rosidl_runtime_c/primitives_sequence_functions.h"

bool
robot_msgs__msg__RobotState__init(robot_msgs__msg__RobotState * msg)
{
  if (!msg) {
    return false;
  }
  // angles
  if (!rosidl_runtime_c__float__Sequence__init(&msg->angles, 0)) {
    robot_msgs__msg__RobotState__fini(msg);
    return false;
  }
  // position_code
  // positions
  if (!rosidl_runtime_c__float__Sequence__init(&msg->positions, 0)) {
    robot_msgs__msg__RobotState__fini(msg);
    return false;
  }
  // temperatures
  if (!rosidl_runtime_c__int32__Sequence__init(&msg->temperatures, 0)) {
    robot_msgs__msg__RobotState__fini(msg);
    return false;
  }
  return true;
}

void
robot_msgs__msg__RobotState__fini(robot_msgs__msg__RobotState * msg)
{
  if (!msg) {
    return;
  }
  // angles
  rosidl_runtime_c__float__Sequence__fini(&msg->angles);
  // position_code
  // positions
  rosidl_runtime_c__float__Sequence__fini(&msg->positions);
  // temperatures
  rosidl_runtime_c__int32__Sequence__fini(&msg->temperatures);
}

bool
robot_msgs__msg__RobotState__are_equal(const robot_msgs__msg__RobotState * lhs, const robot_msgs__msg__RobotState * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // angles
  if (!rosidl_runtime_c__float__Sequence__are_equal(
      &(lhs->angles), &(rhs->angles)))
  {
    return false;
  }
  // position_code
  if (lhs->position_code != rhs->position_code) {
    return false;
  }
  // positions
  if (!rosidl_runtime_c__float__Sequence__are_equal(
      &(lhs->positions), &(rhs->positions)))
  {
    return false;
  }
  // temperatures
  if (!rosidl_runtime_c__int32__Sequence__are_equal(
      &(lhs->temperatures), &(rhs->temperatures)))
  {
    return false;
  }
  return true;
}

bool
robot_msgs__msg__RobotState__copy(
  const robot_msgs__msg__RobotState * input,
  robot_msgs__msg__RobotState * output)
{
  if (!input || !output) {
    return false;
  }
  // angles
  if (!rosidl_runtime_c__float__Sequence__copy(
      &(input->angles), &(output->angles)))
  {
    return false;
  }
  // position_code
  output->position_code = input->position_code;
  // positions
  if (!rosidl_runtime_c__float__Sequence__copy(
      &(input->positions), &(output->positions)))
  {
    return false;
  }
  // temperatures
  if (!rosidl_runtime_c__int32__Sequence__copy(
      &(input->temperatures), &(output->temperatures)))
  {
    return false;
  }
  return true;
}

robot_msgs__msg__RobotState *
robot_msgs__msg__RobotState__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  robot_msgs__msg__RobotState * msg = (robot_msgs__msg__RobotState *)allocator.allocate(sizeof(robot_msgs__msg__RobotState), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(robot_msgs__msg__RobotState));
  bool success = robot_msgs__msg__RobotState__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
robot_msgs__msg__RobotState__destroy(robot_msgs__msg__RobotState * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    robot_msgs__msg__RobotState__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
robot_msgs__msg__RobotState__Sequence__init(robot_msgs__msg__RobotState__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  robot_msgs__msg__RobotState * data = NULL;

  if (size) {
    data = (robot_msgs__msg__RobotState *)allocator.zero_allocate(size, sizeof(robot_msgs__msg__RobotState), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = robot_msgs__msg__RobotState__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        robot_msgs__msg__RobotState__fini(&data[i - 1]);
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
robot_msgs__msg__RobotState__Sequence__fini(robot_msgs__msg__RobotState__Sequence * array)
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
      robot_msgs__msg__RobotState__fini(&array->data[i]);
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

robot_msgs__msg__RobotState__Sequence *
robot_msgs__msg__RobotState__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  robot_msgs__msg__RobotState__Sequence * array = (robot_msgs__msg__RobotState__Sequence *)allocator.allocate(sizeof(robot_msgs__msg__RobotState__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = robot_msgs__msg__RobotState__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
robot_msgs__msg__RobotState__Sequence__destroy(robot_msgs__msg__RobotState__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    robot_msgs__msg__RobotState__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
robot_msgs__msg__RobotState__Sequence__are_equal(const robot_msgs__msg__RobotState__Sequence * lhs, const robot_msgs__msg__RobotState__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!robot_msgs__msg__RobotState__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
robot_msgs__msg__RobotState__Sequence__copy(
  const robot_msgs__msg__RobotState__Sequence * input,
  robot_msgs__msg__RobotState__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(robot_msgs__msg__RobotState);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    robot_msgs__msg__RobotState * data =
      (robot_msgs__msg__RobotState *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!robot_msgs__msg__RobotState__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          robot_msgs__msg__RobotState__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!robot_msgs__msg__RobotState__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
