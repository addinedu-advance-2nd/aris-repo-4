// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from robot_msgs:msg/UserOrder.idl
// generated code does not contain a copyright notice

#ifndef ROBOT_MSGS__MSG__DETAIL__USER_ORDER__STRUCT_HPP_
#define ROBOT_MSGS__MSG__DETAIL__USER_ORDER__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


#ifndef _WIN32
# define DEPRECATED__robot_msgs__msg__UserOrder __attribute__((deprecated))
#else
# define DEPRECATED__robot_msgs__msg__UserOrder __declspec(deprecated)
#endif

namespace robot_msgs
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct UserOrder_
{
  using Type = UserOrder_<ContainerAllocator>;

  explicit UserOrder_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->action = "";
      this->icecream = "";
      this->topping = "";
      this->topping_type = "";
    }
  }

  explicit UserOrder_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : action(_alloc),
    icecream(_alloc),
    topping(_alloc),
    topping_type(_alloc)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->action = "";
      this->icecream = "";
      this->topping = "";
      this->topping_type = "";
    }
  }

  // field types and members
  using _action_type =
    std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>;
  _action_type action;
  using _icecream_type =
    std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>;
  _icecream_type icecream;
  using _topping_type =
    std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>;
  _topping_type topping;
  using _topping_type_type =
    std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>;
  _topping_type_type topping_type;

  // setters for named parameter idiom
  Type & set__action(
    const std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>> & _arg)
  {
    this->action = _arg;
    return *this;
  }
  Type & set__icecream(
    const std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>> & _arg)
  {
    this->icecream = _arg;
    return *this;
  }
  Type & set__topping(
    const std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>> & _arg)
  {
    this->topping = _arg;
    return *this;
  }
  Type & set__topping_type(
    const std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>> & _arg)
  {
    this->topping_type = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    robot_msgs::msg::UserOrder_<ContainerAllocator> *;
  using ConstRawPtr =
    const robot_msgs::msg::UserOrder_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<robot_msgs::msg::UserOrder_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<robot_msgs::msg::UserOrder_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      robot_msgs::msg::UserOrder_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<robot_msgs::msg::UserOrder_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      robot_msgs::msg::UserOrder_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<robot_msgs::msg::UserOrder_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<robot_msgs::msg::UserOrder_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<robot_msgs::msg::UserOrder_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__robot_msgs__msg__UserOrder
    std::shared_ptr<robot_msgs::msg::UserOrder_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__robot_msgs__msg__UserOrder
    std::shared_ptr<robot_msgs::msg::UserOrder_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const UserOrder_ & other) const
  {
    if (this->action != other.action) {
      return false;
    }
    if (this->icecream != other.icecream) {
      return false;
    }
    if (this->topping != other.topping) {
      return false;
    }
    if (this->topping_type != other.topping_type) {
      return false;
    }
    return true;
  }
  bool operator!=(const UserOrder_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct UserOrder_

// alias to use template instance with default allocator
using UserOrder =
  robot_msgs::msg::UserOrder_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace robot_msgs

#endif  // ROBOT_MSGS__MSG__DETAIL__USER_ORDER__STRUCT_HPP_
