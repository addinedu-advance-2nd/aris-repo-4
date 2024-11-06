// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from robot_msgs:action/RobotOrder.idl
// generated code does not contain a copyright notice

#ifndef ROBOT_MSGS__ACTION__DETAIL__ROBOT_ORDER__BUILDER_HPP_
#define ROBOT_MSGS__ACTION__DETAIL__ROBOT_ORDER__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "robot_msgs/action/detail/robot_order__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace robot_msgs
{

namespace action
{

namespace builder
{

class Init_RobotOrder_Goal_topping_type
{
public:
  explicit Init_RobotOrder_Goal_topping_type(::robot_msgs::action::RobotOrder_Goal & msg)
  : msg_(msg)
  {}
  ::robot_msgs::action::RobotOrder_Goal topping_type(::robot_msgs::action::RobotOrder_Goal::_topping_type_type arg)
  {
    msg_.topping_type = std::move(arg);
    return std::move(msg_);
  }

private:
  ::robot_msgs::action::RobotOrder_Goal msg_;
};

class Init_RobotOrder_Goal_topping_num
{
public:
  explicit Init_RobotOrder_Goal_topping_num(::robot_msgs::action::RobotOrder_Goal & msg)
  : msg_(msg)
  {}
  Init_RobotOrder_Goal_topping_type topping_num(::robot_msgs::action::RobotOrder_Goal::_topping_num_type arg)
  {
    msg_.topping_num = std::move(arg);
    return Init_RobotOrder_Goal_topping_type(msg_);
  }

private:
  ::robot_msgs::action::RobotOrder_Goal msg_;
};

class Init_RobotOrder_Goal_tray_num
{
public:
  explicit Init_RobotOrder_Goal_tray_num(::robot_msgs::action::RobotOrder_Goal & msg)
  : msg_(msg)
  {}
  Init_RobotOrder_Goal_topping_num tray_num(::robot_msgs::action::RobotOrder_Goal::_tray_num_type arg)
  {
    msg_.tray_num = std::move(arg);
    return Init_RobotOrder_Goal_topping_num(msg_);
  }

private:
  ::robot_msgs::action::RobotOrder_Goal msg_;
};

class Init_RobotOrder_Goal_order_type
{
public:
  Init_RobotOrder_Goal_order_type()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_RobotOrder_Goal_tray_num order_type(::robot_msgs::action::RobotOrder_Goal::_order_type_type arg)
  {
    msg_.order_type = std::move(arg);
    return Init_RobotOrder_Goal_tray_num(msg_);
  }

private:
  ::robot_msgs::action::RobotOrder_Goal msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::robot_msgs::action::RobotOrder_Goal>()
{
  return robot_msgs::action::builder::Init_RobotOrder_Goal_order_type();
}

}  // namespace robot_msgs


namespace robot_msgs
{

namespace action
{

namespace builder
{

class Init_RobotOrder_Result_result
{
public:
  Init_RobotOrder_Result_result()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::robot_msgs::action::RobotOrder_Result result(::robot_msgs::action::RobotOrder_Result::_result_type arg)
  {
    msg_.result = std::move(arg);
    return std::move(msg_);
  }

private:
  ::robot_msgs::action::RobotOrder_Result msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::robot_msgs::action::RobotOrder_Result>()
{
  return robot_msgs::action::builder::Init_RobotOrder_Result_result();
}

}  // namespace robot_msgs


namespace robot_msgs
{

namespace action
{

namespace builder
{

class Init_RobotOrder_Feedback_message
{
public:
  Init_RobotOrder_Feedback_message()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::robot_msgs::action::RobotOrder_Feedback message(::robot_msgs::action::RobotOrder_Feedback::_message_type arg)
  {
    msg_.message = std::move(arg);
    return std::move(msg_);
  }

private:
  ::robot_msgs::action::RobotOrder_Feedback msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::robot_msgs::action::RobotOrder_Feedback>()
{
  return robot_msgs::action::builder::Init_RobotOrder_Feedback_message();
}

}  // namespace robot_msgs


namespace robot_msgs
{

namespace action
{

namespace builder
{

class Init_RobotOrder_SendGoal_Request_goal
{
public:
  explicit Init_RobotOrder_SendGoal_Request_goal(::robot_msgs::action::RobotOrder_SendGoal_Request & msg)
  : msg_(msg)
  {}
  ::robot_msgs::action::RobotOrder_SendGoal_Request goal(::robot_msgs::action::RobotOrder_SendGoal_Request::_goal_type arg)
  {
    msg_.goal = std::move(arg);
    return std::move(msg_);
  }

private:
  ::robot_msgs::action::RobotOrder_SendGoal_Request msg_;
};

class Init_RobotOrder_SendGoal_Request_goal_id
{
public:
  Init_RobotOrder_SendGoal_Request_goal_id()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_RobotOrder_SendGoal_Request_goal goal_id(::robot_msgs::action::RobotOrder_SendGoal_Request::_goal_id_type arg)
  {
    msg_.goal_id = std::move(arg);
    return Init_RobotOrder_SendGoal_Request_goal(msg_);
  }

private:
  ::robot_msgs::action::RobotOrder_SendGoal_Request msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::robot_msgs::action::RobotOrder_SendGoal_Request>()
{
  return robot_msgs::action::builder::Init_RobotOrder_SendGoal_Request_goal_id();
}

}  // namespace robot_msgs


namespace robot_msgs
{

namespace action
{

namespace builder
{

class Init_RobotOrder_SendGoal_Response_stamp
{
public:
  explicit Init_RobotOrder_SendGoal_Response_stamp(::robot_msgs::action::RobotOrder_SendGoal_Response & msg)
  : msg_(msg)
  {}
  ::robot_msgs::action::RobotOrder_SendGoal_Response stamp(::robot_msgs::action::RobotOrder_SendGoal_Response::_stamp_type arg)
  {
    msg_.stamp = std::move(arg);
    return std::move(msg_);
  }

private:
  ::robot_msgs::action::RobotOrder_SendGoal_Response msg_;
};

class Init_RobotOrder_SendGoal_Response_accepted
{
public:
  Init_RobotOrder_SendGoal_Response_accepted()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_RobotOrder_SendGoal_Response_stamp accepted(::robot_msgs::action::RobotOrder_SendGoal_Response::_accepted_type arg)
  {
    msg_.accepted = std::move(arg);
    return Init_RobotOrder_SendGoal_Response_stamp(msg_);
  }

private:
  ::robot_msgs::action::RobotOrder_SendGoal_Response msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::robot_msgs::action::RobotOrder_SendGoal_Response>()
{
  return robot_msgs::action::builder::Init_RobotOrder_SendGoal_Response_accepted();
}

}  // namespace robot_msgs


namespace robot_msgs
{

namespace action
{

namespace builder
{

class Init_RobotOrder_GetResult_Request_goal_id
{
public:
  Init_RobotOrder_GetResult_Request_goal_id()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::robot_msgs::action::RobotOrder_GetResult_Request goal_id(::robot_msgs::action::RobotOrder_GetResult_Request::_goal_id_type arg)
  {
    msg_.goal_id = std::move(arg);
    return std::move(msg_);
  }

private:
  ::robot_msgs::action::RobotOrder_GetResult_Request msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::robot_msgs::action::RobotOrder_GetResult_Request>()
{
  return robot_msgs::action::builder::Init_RobotOrder_GetResult_Request_goal_id();
}

}  // namespace robot_msgs


namespace robot_msgs
{

namespace action
{

namespace builder
{

class Init_RobotOrder_GetResult_Response_result
{
public:
  explicit Init_RobotOrder_GetResult_Response_result(::robot_msgs::action::RobotOrder_GetResult_Response & msg)
  : msg_(msg)
  {}
  ::robot_msgs::action::RobotOrder_GetResult_Response result(::robot_msgs::action::RobotOrder_GetResult_Response::_result_type arg)
  {
    msg_.result = std::move(arg);
    return std::move(msg_);
  }

private:
  ::robot_msgs::action::RobotOrder_GetResult_Response msg_;
};

class Init_RobotOrder_GetResult_Response_status
{
public:
  Init_RobotOrder_GetResult_Response_status()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_RobotOrder_GetResult_Response_result status(::robot_msgs::action::RobotOrder_GetResult_Response::_status_type arg)
  {
    msg_.status = std::move(arg);
    return Init_RobotOrder_GetResult_Response_result(msg_);
  }

private:
  ::robot_msgs::action::RobotOrder_GetResult_Response msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::robot_msgs::action::RobotOrder_GetResult_Response>()
{
  return robot_msgs::action::builder::Init_RobotOrder_GetResult_Response_status();
}

}  // namespace robot_msgs


namespace robot_msgs
{

namespace action
{

namespace builder
{

class Init_RobotOrder_FeedbackMessage_feedback
{
public:
  explicit Init_RobotOrder_FeedbackMessage_feedback(::robot_msgs::action::RobotOrder_FeedbackMessage & msg)
  : msg_(msg)
  {}
  ::robot_msgs::action::RobotOrder_FeedbackMessage feedback(::robot_msgs::action::RobotOrder_FeedbackMessage::_feedback_type arg)
  {
    msg_.feedback = std::move(arg);
    return std::move(msg_);
  }

private:
  ::robot_msgs::action::RobotOrder_FeedbackMessage msg_;
};

class Init_RobotOrder_FeedbackMessage_goal_id
{
public:
  Init_RobotOrder_FeedbackMessage_goal_id()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_RobotOrder_FeedbackMessage_feedback goal_id(::robot_msgs::action::RobotOrder_FeedbackMessage::_goal_id_type arg)
  {
    msg_.goal_id = std::move(arg);
    return Init_RobotOrder_FeedbackMessage_feedback(msg_);
  }

private:
  ::robot_msgs::action::RobotOrder_FeedbackMessage msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::robot_msgs::action::RobotOrder_FeedbackMessage>()
{
  return robot_msgs::action::builder::Init_RobotOrder_FeedbackMessage_goal_id();
}

}  // namespace robot_msgs

#endif  // ROBOT_MSGS__ACTION__DETAIL__ROBOT_ORDER__BUILDER_HPP_
